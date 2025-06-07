import os
import cv2
from ultralytics import YOLO

# --- CONFIGURATION ---
video_path = "/Users/dhanviannam/Documents/IIIT H proj/T2/input1.mp4"
frames_folder = "/Users/dhanviannam/Documents/IIIT H proj/T2/input_images"
segmented_output_folder = "/Users/dhanviannam/Documents/IIIT H proj/T2/segmented_images"
final_video_path = "/Users/dhanviannam/Documents/IIIT H proj/T2/segmented_video.mp4"
model_path = "yolov8s-seg.pt"  # It will download automatically if not available
frame_interval = 5  # Save every 5th frame

# --- CREATE FOLDERS ---
os.makedirs(frames_folder, exist_ok=True)
os.makedirs(segmented_output_folder, exist_ok=True)

# --- EXTRACT FRAMES FROM VIDEO ---
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise IOError("❌ Could not open video file: " + video_path)

print("🎬 Extracting frames from video...")
frame_count = 0
saved_count = 0

while True:
    success, frame = cap.read()
    if not success:
        break
    if frame_count % frame_interval == 0:
        filename = f"frame_{saved_count:04d}.jpg"
        filepath = os.path.join(frames_folder, filename)
        cv2.imwrite(filepath, frame)
        print(f"✅ Saved {filename}")
        saved_count += 1
    frame_count += 1

cap.release()

# --- LOAD YOLOv8 MODEL ---
model = YOLO(model_path)

# --- SEGMENT EXTRACTED FRAMES ---
image_files = [f for f in sorted(os.listdir(frames_folder)) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

if not image_files:
    raise RuntimeError("No extracted frames found in: " + frames_folder)

print("🧠 Segmenting extracted frames...")
for img_file in image_files:
    img_path = os.path.join(frames_folder, img_file)
    results = model(img_path, save=True, project=segmented_output_folder, name="seg_output", exist_ok=True)
    print(f"🟢 Segmented: {img_file}")

# --- GATHER SEGMENTED IMAGES FOR VIDEO ---
seg_results_folder = os.path.join(segmented_output_folder, "seg_output")
seg_images = [f for f in sorted(os.listdir(seg_results_folder)) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

if not seg_images:
    raise RuntimeError("No segmented images found to create video.")

# --- SETUP VIDEO WRITER ---
first_img_path = os.path.join(seg_results_folder, seg_images[0])
first_frame = cv2.imread(first_img_path)
height, width, _ = first_frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(final_video_path, fourcc, 10, (width, height))

print("🎞️ Creating final video from segmented images...")
for img_name in seg_images:
    img_path = os.path.join(seg_results_folder, img_name)
    frame = cv2.imread(img_path)
    video_writer.write(frame)

video_writer.release()

print(f"\n🎉 Done! Final segmented video saved at:\n{final_video_path}")
