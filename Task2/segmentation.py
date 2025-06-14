from ultralytics import YOLO
import os
from PIL import Image

model = YOLO("yolov8n-seg.pt")  # Use 'yolov8s-seg.pt' or others based on your setup

folder_path = "/Users/dhanviannam/Documents/IIIT H proj/images"
output_path = "/Users/dhanviannam/Documents/IIIT H proj/output"

os.makedirs(output_path, exist_ok=True)

image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

for file in image_files:
    img_path = os.path.join(folder_path, file)
    results = model(img_path, save=True, project=output_path, name="seg_results", exist_ok=True)
    print("Processing:", img_path)

