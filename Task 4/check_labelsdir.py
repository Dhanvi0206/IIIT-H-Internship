import os

label_root = "/Users/dhanviannam/Documents/IIIT H proj/Task 4/dataset/labels"

if not os.path.exists(label_root):
    print(f"❌ labels folder does not exist: {label_root}")
else:
    print(f"📂 Contents of 'labels/':")
    print(os.listdir(label_root))
