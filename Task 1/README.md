# IIIT-H-Internship

-->Object Detection using YOLOv8 on an Image from URL

This project demonstrates how to perform object detection using [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) on an image from a public URL.
We use the image [`https://ultralytics.com/images/bus.jpg`](https://ultralytics.com/images/bus.jpg) and detect objects like people, cars, buses, etc., with bounding boxes and labels.
 Sample Image:
[bus](https://ultralytics.com/images/bus.jpg)
System Requirements:
- Python 3.8+
- pip
Python Packages Used:

| Package      | Purpose                          |
|--------------|----------------------------------|
| `ultralytics`| For using YOLOv8 model           |
| `requests`   | Download image from a URL        |
| `Pillow`     | Open and manipulate images       |

---
Installation:

1. Clone the repository (or create your own Python script)
2. Install dependencies:

```bash
pip install ultralytics pillow requests
