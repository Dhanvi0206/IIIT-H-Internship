Task1:
└── segmentation.py
Task2:
└── video_segmentation_yolov8.py
Task3:
└── video_frame_extractor.py

Task Details:

Task 1: Semantic Segmentation Overlay

**File**: `segmentation.py`

- Visualizes model-predicted segmentation masks by overlaying them on original images.
- Color maps help distinguish different classes in the segmented output.
- Saves and displays the output as a combined image.
- Useful for **model evaluation** in segmentation tasks.

Task 2: YOLOv8 Detection Visualization

**File**: `video_segmentation_yolov8.py`

- Parses YOLO-formatted `.txt` annotation files.
- Draws bounding boxes and confidence scores on the image using OpenCV.
- Supports batch visualization for dataset review.
- Helpful for **object detection result verification**.

Task 3: Video to Frame Extractor

**File**: `video_frame_extractor.py`

- Loads a video file and extracts frames at fixed intervals.
- Saves frames to disk for use in training or testing computer vision models.
- Allows frame skipping (e.g., extract every 10th frame).
- Useful in **preprocessing datasets** for action recognition, tracking, etc.

---
Requirements

Install the required libraries using:

```bash
pip install opencv-python matplotlib pillow
