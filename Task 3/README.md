African Wildlife Detection using YOLOv8;

This repository contains a training script for object detection on the **African Wildlife** dataset using the **YOLOv8** architecture.

Script
`train_african_wildlife_yolo.py`

Trains a YOLOv8 model using the Ultralytics framework with a custom 4-class dataset. It supports model configuration, training, validation, and automatic logging of results.

Dataset

- Name: African Wildlife  
- Classes: Elephant, Giraffe, Zebra, Lion  
- Format: YOLOv5/YOLOv8 style (with `.yaml` configuration)  
- Source: [Ultralytics African Wildlife Dataset](https://docs.ultralytics.com/datasets/detect/african-wildlife/)

Setup & Execution:

Install required libraries:
bash:
'pip install ultralytics opencv-python'

Output
After training, results will be saved in runs/detect/train/, including:

🔹 Model Weights
best.pt: Best performing weights (based on validation metrics)
last.pt: Weights from the final epoch

🔹 Visualizations
results.png: Graph of training & validation loss, precision, recall, mAP
confusion_matrix.png: Confusion matrix of class-wise predictions
F1_curve.png: F1-score progression
PR_curve.png: Precision-Recall curve
labels.jpg: Dataset label distribution

🔹 Logs
Training progress logs in terminal or results.csv
Evaluation metrics:
mAP@0.5
mAP@0.5:0.95

Precision & Recall per class:

These outputs help you understand the model’s learning behavior and evaluate performance on unseen validation data.


