from ultralytics import YOLO
from PIL import Image

# Load YOLOv8 model (you can use 'yolov8n.pt', 'yolov8s.pt', etc.)
model = YOLO('yolov8n.pt')

# Load your saved image
img = Image.open('image.jpg').convert("RGB")  # Ensure RGB format

# Run object detection
results = model(img)

# Display results (with bounding boxes)
results[0].show()

# Optionally save the result image
results
