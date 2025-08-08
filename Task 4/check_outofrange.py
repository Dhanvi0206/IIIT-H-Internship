# Scan all train labels and show out-of-range classes
import os

label_dir = '/Users/dhanviannam/Documents/IIIT H proj/Task 4/dataset/labels/train'
out_of_range = set()
for file in os.listdir(label_dir):
    if file.endswith('.txt'):
        with open(os.path.join(label_dir, file)) as f:
            for line in f:
                if line.strip() and line[0].isdigit():
                    class_id = int(line.split()[0])
                    if class_id > 24:
                        out_of_range.add((file, class_id))

print("Labels with class ID > 24:", out_of_range)
