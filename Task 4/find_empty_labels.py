import os

label_dir = '/Users/dhanviannam/Documents/IIIT H proj/Task 4/dataset/labels/train'
empty_files = []

for f in os.listdir(label_dir):
    path = os.path.join(label_dir, f)
    if os.path.getsize(path) == 0:
        empty_files.append(f)

print(f"Empty label files: {len(empty_files)}")
print(empty_files)
