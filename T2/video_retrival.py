import os
import cv2
from ultralytics import YOLO

# --- CONFIGURATION ---
input_images = "/Users/dhanviannam/Documents/IIIT H proj/T2/input_images"  # Folder with original images
segmented_output_folder = "/Users/dhanviannam/Documents/IIIT H proj/T2/segmented_images"  # Where segmented images go
final_video_path = "/Users/dhanviannam/Documents/IIIT H proj/T2/segmented_video.mp4"  # Output video
model_path = "yolov8s-seg.pt"  # Auto downloads if not present

# --- SETUP ---
os.makedirs(segmented_output_folder, exist_ok=True)

# --- LOAD MODEL ---
model = YOLO(model_path)

# --- SEGMENT IMAGES ---
image_files = [f for f in sorted(os.listdir(input_images)) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

if not image_files:
    raise RuntimeError("No input images found in the folder: " + input_images)

print(f"🔍 Found {len(image_files)} images. Starting segmentation...")

for img_file in image_files:
    img_path = os.path.join(input_images, img_file)
    results = model(img_path, save=True, project=segmented_output_folder, name="seg_output", exist_ok=True)
    print(f"✅ Segmented: {img_file}")

# --- COLLECT SEGMENTED IMAGES FOR VIDEO ---
seg_results_folder = os.path.join(segmented_output_folder, "seg_output")
seg_images = [f for f in sorted(os.listdir(seg_results_folder)) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

if not seg_images:
    raise RuntimeError("No segmented images found to create video.")

# --- GET VIDEO SIZE ---
first_img_path = os.path.join(seg_results_folder, seg_images[0])
first_frame = cv2.imread(first_img_path)
height, width, _ = first_frame.shape

# --- CREATE VIDEO ---
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(final_video_path, fourcc, 10, (width, height))

print("🎞️ Creating video from segmented images...")

for img_name in seg_images:
    img_path = os.path.join(seg_results_folder, img_name)
    frame = cv2.imread(img_path)
    video_writer.write(frame)

video_writer.release()

print(f"\n🎉 Done! Segmented video saved at: {final_video_path}")
