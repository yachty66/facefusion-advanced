#!/usr/bin/env python3
import os
import subprocess
import re
import time
import json
import pandas as pd  # Added pandas import
import glob  # Add this import

# Paths
VIDEOS_DIR = "images/videos"
RESULTS_DIR = "images/results"
LOGS_DIR = "images/results/logs"

# Create directories if they don't exist
os.makedirs(LOGS_DIR, exist_ok=True)

# Clear existing log files to ensure fresh data
print("Clearing previous log files...")
for old_log_file in glob.glob(os.path.join(LOGS_DIR, "*_execution_logs.md")):
    try:
        os.remove(old_log_file)
        print(f"Removed old log file: {old_log_file}")
    except Exception as e:
        print(f"Failed to remove {old_log_file}: {e}")

# Remove previous summary file if it exists
summary_file = os.path.join(RESULTS_DIR, "video_processing_summary.csv")
if os.path.exists(summary_file):
    try:
        os.remove(summary_file)
        print(f"Removed old summary file: {summary_file}")
    except Exception as e:
        print(f"Failed to remove {summary_file}: {e}")

# Videos to process (1-10)
VIDEOS = [f"vid{i}.mp4" for i in range(1, 11)]

# Function to extract metrics from log output
def extract_metrics(log_output, video_name):
    metrics = {
        "Video_Name": video_name,
        "Resolution": "",
        "Frame_Rate": 0,
        "Total_Frames": 0,
        "Total_Processing_Time": 0,
        "Frame_Extraction_Speed": 0,
        "Face_Processing_Speed": 0,
        "Video_Merging_Speed": 0,
        "Execution_Providers": "CUDA",
        "Frames_with_Faces": 0,
        "Frames_with_Faces_Percentage": 0,
        "Frames_without_Faces": 0,
        "Frames_without_Faces_Percentage": 0,
        "Total_Faces_Detected": 0,
        "Faces_per_Frame_avg": 0,
        "Angle_0_Success_Frames": 0,
        "Angle_0_Success_Percentage": 0,
        "Angle_90_Success_Frames": 0, 
        "Angle_90_Success_Percentage": 0,
        "Angle_270_Success_Frames": 0,
        "Angle_270_Success_Percentage": 0,
        "Multiple_Angles_Required_Frames": 0,
        "Multiple_Angles_Required_Percentage": 0,
        "Min_Face_Detector_Score": 0,
        "Max_Face_Detector_Score": 0,
        "Avg_Face_Detector_Score": 0,
        "Min_Face_Landmarker_Score": 0,
        "Max_Face_Landmarker_Score": 0,
        "Avg_Face_Landmarker_Score": 0,
        "Primary_Bottleneck": "",
        "Primary_Bottleneck_Speed": 0,
        "Secondary_Bottleneck": "",
        "Secondary_Bottleneck_Speed": 0
    }
    
    # Extract resolution and FPS
    res_match = re.search(r"resolution of (\d+x\d+) and (\d+\.\d+) frames per second", log_output)
    if res_match:
        metrics["Resolution"] = res_match.group(1)
        metrics["Frame_Rate"] = float(res_match.group(2))
    
    # Extract total processing time
    time_match = re.search(r"Processing to video succeed in (\d+\.\d+) seconds", log_output)
    if time_match:
        metrics["Total_Processing_Time"] = float(time_match.group(1))
    
    # Extract extraction, processing and merging speeds
    extract_match = re.search(r"Extracting:.+?(\d+\.\d+)frame/s", log_output)
    if extract_match:
        metrics["Frame_Extraction_Speed"] = float(extract_match.group(1))
    
    process_match = re.search(r"Processing: 100%.+?(\d+\.\d+)frame/s", log_output)
    if process_match:
        metrics["Face_Processing_Speed"] = float(process_match.group(1))
    
    merge_match = re.search(r"Merging:.+?(\d+\.\d+)frame/s", log_output)
    if merge_match:
        metrics["Video_Merging_Speed"] = float(merge_match.group(1))
    
    # Extract total frames
    frames_match = re.search(r"(\d+)/\1 \[", log_output)
    if frames_match:
        metrics["Total_Frames"] = int(frames_match.group(1))
    
    # Extract face detection stats
    faces_match = re.search(r"total_frames_with_faces: (\d+)", log_output)
    if faces_match:
        metrics["Frames_with_Faces"] = int(faces_match.group(1))
        if metrics["Total_Frames"] > 0:
            metrics["Frames_with_Faces_Percentage"] = round(metrics["Frames_with_Faces"] / metrics["Total_Frames"] * 100)
            metrics["Frames_without_Faces"] = metrics["Total_Frames"] - metrics["Frames_with_Faces"]
            metrics["Frames_without_Faces_Percentage"] = 100 - metrics["Frames_with_Faces_Percentage"]
    
    total_faces_match = re.search(r"total_faces: (\d+)", log_output)
    if total_faces_match:
        metrics["Total_Faces_Detected"] = int(total_faces_match.group(1))
        if metrics["Frames_with_Faces"] > 0:
            metrics["Faces_per_Frame_avg"] = round(metrics["Total_Faces_Detected"] / metrics["Frames_with_Faces"], 1)
    
    # Count angle successes
    angle_0_success = len(re.findall(r"FOUND \d+ FACES AT ANGLE 0", log_output))
    angle_90_success = len(re.findall(r"FOUND \d+ FACES AT ANGLE 90", log_output))
    angle_270_success = len(re.findall(r"FOUND \d+ FACES AT ANGLE 270", log_output))
    
    metrics["Angle_0_Success_Frames"] = angle_0_success
    metrics["Angle_90_Success_Frames"] = angle_90_success
    metrics["Angle_270_Success_Frames"] = angle_270_success
    
    if metrics["Total_Frames"] > 0:
        metrics["Angle_0_Success_Percentage"] = round(angle_0_success / metrics["Total_Frames"] * 100)
        metrics["Angle_90_Success_Percentage"] = round(angle_90_success / metrics["Total_Frames"] * 100)
        metrics["Angle_270_Success_Percentage"] = round(angle_270_success / metrics["Total_Frames"] * 100)
    
    # Extract face quality metrics
    min_detector_match = re.search(r"min_face_detector_score: (\d+\.\d+)", log_output)
    if min_detector_match:
        metrics["Min_Face_Detector_Score"] = float(min_detector_match.group(1))
    
    max_detector_match = re.search(r"max_face_detector_score: (\d+\.\d+)", log_output)
    if max_detector_match:
        metrics["Max_Face_Detector_Score"] = float(max_detector_match.group(1))
    
    avg_detector_match = re.search(r"average_face_detector_score: (\d+\.\d+)", log_output)
    if avg_detector_match:
        metrics["Avg_Face_Detector_Score"] = float(avg_detector_match.group(1))
    
    min_landmarker_match = re.search(r"min_face_landmarker_score: (\d+\.\d+)", log_output)
    if min_landmarker_match:
        metrics["Min_Face_Landmarker_Score"] = float(min_landmarker_match.group(1))
    
    max_landmarker_match = re.search(r"max_face_landmarker_score: (\d+\.\d+)", log_output)
    if max_landmarker_match:
        metrics["Max_Face_Landmarker_Score"] = float(max_landmarker_match.group(1))
    
    avg_landmarker_match = re.search(r"average_face_landmarker_score: (\d+\.\d+)", log_output)
    if avg_landmarker_match:
        metrics["Avg_Face_Landmarker_Score"] = float(avg_landmarker_match.group(1))
    
    # Determine bottlenecks
    speeds = [
        ("Frame_Extraction", metrics["Frame_Extraction_Speed"]),
        ("Face_Processing", metrics["Face_Processing_Speed"]),
        ("Video_Merging", metrics["Video_Merging_Speed"])
    ]
    speeds.sort(key=lambda x: x[1])
    
    if len(speeds) >= 1:
        metrics["Primary_Bottleneck"] = speeds[0][0]
        metrics["Primary_Bottleneck_Speed"] = speeds[0][1]
    
    if len(speeds) >= 2:
        metrics["Secondary_Bottleneck"] = speeds[1][0]
        metrics["Secondary_Bottleneck_Speed"] = speeds[1][1]
    
    return metrics

# Function to create metrics file
def save_metrics_file(metrics, output_file):
    with open(output_file, 'w') as f:
        for key, value in metrics.items():
            f.write(f"{key},{value}\n")

# List to store all metrics for summary
all_metrics = []

# Process each video
for video in VIDEOS:
    print(f"Processing {video}...")
    video_path = os.path.join(VIDEOS_DIR, video)
    result_name = f"result_{video}"
    result_path = os.path.join(RESULTS_DIR, result_name)
    
    # Generate log file name from video name
    log_base_name = os.path.splitext(video)[0]
    log_file = os.path.join(LOGS_DIR, f"{log_base_name}_execution_logs.md")
    
    # Check if video exists
    if not os.path.exists(video_path):
        print(f"Video file {video_path} not found. Skipping.")
        continue
        
    # Create a temporary file for FFmpeg
    temp_video_path = os.path.join(VIDEOS_DIR, f"temp_{video}")
    
    # Run FFmpeg first to fix potential video corruption
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", video_path, "-c:v", "libx264", "-crf", "18", temp_video_path
    ]
    
    print(f"Fixing video with FFmpeg: {video_path}")
    try:
        subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Replace the original file with the fixed version
        os.replace(temp_video_path, video_path)
        print(f"Fixed video replaced original: {video_path}")
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error: {e}")
        # Clean up temp file if it exists
        if os.path.exists(temp_video_path):
            os.remove(temp_video_path)
        continue
    
    # Run FaceFusion command with debug logging on the fixed video
    cmd = [
        "python", "facefusion.py", "headless-run",
        "--keep-temp",
        "--log-level", "debug",
        "--execution-providers", "cuda",
        "--execution-thread-count", "16",
        "--execution-queue-count", "2",
        "--video-memory-strategy", "moderate",
        "--temp-frame-format", "jpg",
        "--face-selector-mode", "reference",
        "--face-mask-types", "box", "occlusion",
        "--processors", "face_swapper",
        "--face-swapper-model", "inswapper_128",
        "--face-swapper-pixel-boost", "512x512",
        "--face-detector-model", "retinaface",
        "--face-detector-size", "640x640",
        "--face-detector-score", "0.5",
        "--reference-face-distance", "0.6",
        "--face-mask-blur", "0.5",
        "--output-video-preset", "veryfast",
        "--output-video-quality", "85",
        "-s", "images/image.png",
        "-t", video_path,
        "-o", result_path
    ]
    
    # Capture output
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        
        # Collect the full log output
        log_output = ""
        for line in process.stdout:
            log_output += line
            print(line, end='')  # Show output in real-time
        
        process.wait()
        
        # Check if process completed successfully
        if process.returncode != 0:
            print(f"FaceFusion failed with return code {process.returncode}")
        
        # Extract metrics and save to file even if the process failed
        metrics = extract_metrics(log_output, video)
        save_metrics_file(metrics, log_file)
        
        # Also add to our list for the summary
        all_metrics.append(metrics)
        
        print(f"Metrics saved to {log_file}")
        
    except Exception as e:
        print(f"Error processing {video}: {e}")
        # Create minimal metrics for failed videos
        metrics = {"Video_Name": video, "Error": str(e)}
        for key in extract_metrics("", "").keys():
            if key not in metrics:
                metrics[key] = 0 if isinstance(extract_metrics("", "")[key], (int, float)) else ""
        
        save_metrics_file(metrics, log_file)
        all_metrics.append(metrics)
        print(f"Error metrics saved to {log_file}")
    
    # Add a small delay between videos
    time.sleep(1)

print("Processing complete!")

# Generate combined summary CSV file
print("Generating summary CSV file...")

# Convert metrics list to pandas DataFrame
if all_metrics:
    # Create a DataFrame from all metrics
    df = pd.DataFrame(all_metrics)
    
    # Save to a single CSV file
    summary_file = os.path.join(RESULTS_DIR, "video_processing_summary.csv")
    df.to_csv(summary_file, index=False)
    
    print(f"Summary saved to {summary_file}")
else:
    print("No metrics collected, skipping summary creation")
