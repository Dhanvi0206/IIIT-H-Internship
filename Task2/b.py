import cv2
import os

# --- CONFIG ---
video_path = "/Users/dhanviannam/Documents/IIIT H proj/T2/input.mp4"  # Your input video path
output_folder = "/Users/dhanviannam/Documents/IIIT H proj/T2/frames"       # Folder to save extracted frames
frame_interval = 5  # Save every 5th frame (adjust as needed)

# --- PREPARE FOLDER ---
os.makedirs(output_folder, exist_ok=True)

# --- OPEN VIDEO ---
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise IOError("Could not open video file: " + video_path)

frame_count = 0
saved_count = 0

# --- FRAME LOOP ---
while True:
    success, frame = cap.read()
    if not success:
        break  # End of video

    if frame_count % frame_interval == 0:
        filename = f"frame_{saved_count:04d}.jpg"
        filepath = os.path.join(output_folder, filename)
        cv2.imwrite(filepath, frame)
        print(f"Saved {filename}")
        saved_count += 1

    frame_count += 1

cap.release()
print(f"\nDone! Saved {saved_count} frames in: {output_folder}")

# --- REBUILD VIDEO FROM FRAMES ---

output_video = "/Users/dhanviannam/Documents/IIIT H proj/T2/output_video.mp4"
fps = 30  # frames per second for output video

images = sorted([img for img in os.listdir(output_folder) if img.endswith(".jpg")])
if not images:
    raise Exception("No frames found to create video.")

first_frame = cv2.imread(os.path.join(output_folder, images[0]))
height, width, _ = first_frame.shape

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

for img_name in images:
    img_path = os.path.join(output_folder, img_name)
    frame = cv2.imread(img_path)
    video_writer.write(frame)

video_writer.release()
print(f"🎉 Video saved as {output_video}")
