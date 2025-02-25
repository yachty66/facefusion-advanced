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
from facefusion.vision import count_video_frame_total, get_video_frame


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

def get_alignment_of_faces(vision_frame: VisionFrame) -> float:
	import os
	import cv2
	from litellm import completion
	import base64
	from dotenv import load_dotenv

	load_dotenv()

	# Convert frame to PNG in memory and encode to base64
	_, buffer = cv2.imencode('.png', vision_frame)
	base64_image = base64.b64encode(buffer).decode('utf-8')

	os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

	# Make API call to vision model
	response = completion(
		model="gpt-4o-mini",
		messages=[
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": "Is the person (or persons) in that image vertically or horizontally aligned? Respond only with the value; if vertical respond with 0 and if horizontal respond with 90. If vertical or horizontal is not appropriate or it's not clear, respond with False but remember nothing else."
					},
					{
						"type": "image_url",
						"image_url": {
							"url": f"data:image/jpeg;base64,{base64_image}"
						}
					}
				]
			}
		],
	)
	if response.choices[0].message.content.strip() == "90":
		#we are setting this value to 270 for now because with our example image this will make the position to be vertical - later we need to find out into which direction we need to turn the image
		return 270
	else:
		return 0

def get_many_faces(vision_frames : List[VisionFrame]) -> List[Face]:
	many_faces : List[Face] = []

	# Get total frames from the video
	video_path = state_manager.get_item('target_path')
	total_frames = count_video_frame_total(video_path)
	# Case where input is image and no video
	if total_frames == 0:
		import cv2
		# Read the target image directly since it's not a video
		target_image = cv2.imread(state_manager.get_item('target_path'))
		alignment_of_faces = get_alignment_of_faces(target_image)
	else:
		middle_frame_number = total_frames // 2
		# Get the middle frame directly from the video
		middle_frame = get_video_frame(video_path, middle_frame_number)
		alignment_of_faces = get_alignment_of_faces(middle_frame)

	# Update the face detector angles based on alignment
	state_manager.set_item('face_detector_angles', [int(alignment_of_faces)])

	for vision_frame in vision_frames:
		if numpy.any(vision_frame):
			static_faces = get_static_faces(vision_frame)
			if static_faces:
				many_faces.extend(static_faces)
			else:
				all_bounding_boxes = []
				all_face_scores = []
				all_face_landmarks_5 = []

				# Now using the updated angles from state_manager
				for face_detector_angle in state_manager.get_item('face_detector_angles'):
					if face_detector_angle == 0:
						bounding_boxes, face_scores, face_landmarks_5 = detect_faces(vision_frame)
					else:
						bounding_boxes, face_scores, face_landmarks_5 = detect_rotated_faces(vision_frame, face_detector_angle)
					all_bounding_boxes.extend(bounding_boxes)
					all_face_scores.extend(face_scores)
					all_face_landmarks_5.extend(face_landmarks_5)

				if all_bounding_boxes and all_face_scores and all_face_landmarks_5 and state_manager.get_item('face_detector_score') > 0:
					faces = create_faces(vision_frame, all_bounding_boxes, all_face_scores, all_face_landmarks_5)

					if faces:
						many_faces.extend(faces)
						set_static_faces(vision_frame, faces)
	return many_faces