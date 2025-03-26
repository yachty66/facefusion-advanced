from typing import List, Optional

import numpy

from facefusion import state_manager
from facefusion.common_helper import get_first
from facefusion.face_classifier import classify_face
from facefusion.face_detector import detect_faces, detect_rotated_faces
from facefusion.face_helper import apply_nms, convert_to_face_landmark_5, estimate_face_angle, get_nms_threshold
from facefusion.face_landmarker import detect_face_landmarks, estimate_face_landmark_68_5
from facefusion.face_recognizer import calc_embedding
from facefusion.face_store import get_static_faces, set_static_faces
from facefusion.typing import BoundingBox, Face, FaceLandmark5, FaceLandmarkSet, FaceScoreSet, Score, VisionFrame


def create_faces(vision_frame : VisionFrame, bounding_boxes : List[BoundingBox], face_scores : List[Score], face_landmarks_5 : List[FaceLandmark5]) -> List[Face]:
	faces = []
	nms_threshold = get_nms_threshold(state_manager.get_item('face_detector_model'), state_manager.get_item('face_detector_angles'))
	keep_indices = apply_nms(bounding_boxes, face_scores, state_manager.get_item('face_detector_score'), nms_threshold)

	for index in keep_indices:
		bounding_box = bounding_boxes[index]
		face_score = face_scores[index]
		face_landmark_5 = face_landmarks_5[index]
		face_landmark_5_68 = face_landmark_5
		face_landmark_68_5 = estimate_face_landmark_68_5(face_landmark_5_68)
		face_landmark_68 = face_landmark_68_5
		face_landmark_score_68 = 0.0
		face_angle = estimate_face_angle(face_landmark_68_5)

		if state_manager.get_item('face_landmarker_score') > 0:
			face_landmark_68, face_landmark_score_68 = detect_face_landmarks(vision_frame, bounding_box, face_angle)
		if face_landmark_score_68 > state_manager.get_item('face_landmarker_score'):
			face_landmark_5_68 = convert_to_face_landmark_5(face_landmark_68)

		face_landmark_set : FaceLandmarkSet =\
		{
			'5': face_landmark_5,
			'5/68': face_landmark_5_68,
			'68': face_landmark_68,
			'68/5': face_landmark_68_5
		}
		face_score_set : FaceScoreSet =\
		{
			'detector': face_score,
			'landmarker': face_landmark_score_68
		}
		embedding, normed_embedding = calc_embedding(vision_frame, face_landmark_set.get('5/68'))
		gender, age, race = classify_face(vision_frame, face_landmark_set.get('5/68'))
		faces.append(Face(
			bounding_box = bounding_box,
			score_set = face_score_set,
			landmark_set = face_landmark_set,
			angle = face_angle,
			embedding = embedding,
			normed_embedding = normed_embedding,
			gender = gender,
			age = age,
			race = race
		))
	return faces


def get_one_face(faces : List[Face], position : int = 0) -> Optional[Face]:
	if faces:
		position = min(position, len(faces) - 1)
		return faces[position]
	return None


def get_average_face(faces : List[Face]) -> Optional[Face]:
	embeddings = []
	normed_embeddings = []

	if faces:
		first_face = get_first(faces)

		for face in faces:
			embeddings.append(face.embedding)
			normed_embeddings.append(face.normed_embedding)

		return Face(
			bounding_box = first_face.bounding_box,
			score_set = first_face.score_set,
			landmark_set = first_face.landmark_set,
			angle = first_face.angle,
			embedding = numpy.mean(embeddings, axis = 0),
			normed_embedding = numpy.mean(normed_embeddings, axis = 0),
			gender = first_face.gender,
			age = first_face.age,
			race = first_face.race
		)
	return None

#17.82
#17.43
#17.53 - with dynamic recognition
#18.22

from concurrent.futures import ThreadPoolExecutor
from typing import Tuple, Optional

def try_angle(vision_frame: VisionFrame, angle: int) -> Tuple[List[Face], int]:
    """Try face detection at a specific angle"""
    print(f"Trying angle {angle} in parallel")
    try:
        if angle == 0:
            bounding_boxes, face_scores, face_landmarks_5 = detect_faces(vision_frame)
        else:
            bounding_boxes, face_scores, face_landmarks_5 = detect_rotated_faces(vision_frame, angle)
        
        if bounding_boxes and face_scores and face_landmarks_5 and state_manager.get_item('face_detector_score') > 0:
            faces = create_faces(vision_frame, bounding_boxes, face_scores, face_landmarks_5)
            if faces:
                return faces, angle
    except Exception as e:
        print(f"Error processing angle {angle}: {str(e)}")
    return [], angle

def parallel_face_detection(vision_frame: VisionFrame, angles: List[int]) -> Tuple[List[Face], int]:
    """Run face detection for all angles in parallel"""
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(try_angle, vision_frame, angle) for angle in angles]
        for future in futures:
            faces, angle = future.result()
            if faces:
                print(f"Found faces at angle {angle}")
                return faces, angle
    return [], 0

def get_many_faces(vision_frames: List[VisionFrame]) -> List[Face]:
    many_faces: List[Face] = []
    last_successful_angle = 0
    
    for index, vision_frame in enumerate(vision_frames):
        print(f"Processing frame {index}")
        if not numpy.any(vision_frame):
            continue
            
        # Check cache first
        static_faces = get_static_faces(vision_frame)
        if static_faces:
            many_faces.extend(static_faces)
            continue
        
        # Prepare angles to try, prioritizing last successful angle
        angles_to_try = [last_successful_angle]
        remaining_angles = [a for a in [0, 90, 270] if a != last_successful_angle]
        angles_to_try.extend(remaining_angles)
        
        # Try all angles in parallel
        faces, successful_angle = parallel_face_detection(vision_frame, angles_to_try)
        
        if faces:
            many_faces.extend(faces)
            set_static_faces(vision_frame, faces)
            last_successful_angle = successful_angle
            print(f"Successfully detected faces in frame {index} at angle {successful_angle}")
        else:
            print(f"No faces detected in frame {index} after trying all angles")

    return many_faces