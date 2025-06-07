from ultralytics import YOLO

# Load a pre-trained YOLO model
model = YOLO('yolov8n.pt')

# Run inference on an image from the web
results = model('https://ultralytics.com/images/bus.jpg')

# Show the results (this opens a window or inline in some environments)
results[0].show()

# Optionally save the annotated image to disk
results[0].save()  # saves image with bounding boxes and masks to ./runs/detect/exp or similar folder
