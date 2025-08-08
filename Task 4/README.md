YOLO Custom Object Detection – Sports & Players Dataset

Task Overview:
This project demonstrates the end-to-end pipeline for building a custom YOLO object detection model.
We created our own dataset, annotated sports-related objects and persons, and trained YOLO to detect them.
The model is capable of detecting multiple players and sports equipment in images.

Dataset Preparation
1️⃣ Image Collection
Gathered images from various sources to cover all 26 labels.
Ensured multiple lighting, angles, and backgrounds for robust detection.

2️⃣ Annotation
Used Makesense.ai for bounding box annotation.
Exported labels in YOLO format (.txt files).
Each .txt file corresponds to an image and contains:
class_id  x_center  y_center  width  height

3️⃣ Dataset Structure
dataset/
├── images/
│   ├── train/
│   ├── val/
│   ├── test/
├── labels/
│   ├── train/
│   ├── val/
│   ├── test/

-->YOLO Configuration: data.yaml file

🚀 Training
->Install YOLO:
pip install ultralytics
->Train the Model:
yolo detect train data=data.yaml model=yolov8n.pt epochs=15 imgsz=100
->Run inference on an image:
yolo detect predict model=runs/detect/train/weights/best.pt source=path/to/image.jpg
->Run evaluation on test set:
yolo detect val model=runs/detect/train/weights/best.pt data=data.yaml split=test

📊 Results
*After training, the model can detect multiple players and sports equipment in real-time.
*Metrics like mAP, Precision, and Recall are recorded in runs/detect/train/


