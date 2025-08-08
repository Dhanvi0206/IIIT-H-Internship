import os
import random
import shutil

# Base dataset directory (adjust if needed)
base_dir = "Task4/dataset"
images_dir = os.path.join(base_dir, "images")
labels_dir = os.path.join(base_dir, "labels")

# Output subdirectories
image_train_dir = os.path.join(images_dir, "train")
image_val_dir = os.path.join(images_dir, "val")
label_train_dir = os.path.join(labels_dir, "train")
label_val_dir = os.path.join(labels_dir, "val")

# Create train/val folders if they don't exist
os.makedirs(image_train_dir, exist_ok=True)
os.makedirs(image_val_dir, exist_ok=True)
os.makedirs(label_train_dir, exist_ok=True)
os.makedirs(label_val_dir, exist_ok=True)

# List all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png')) and os.path.isfile(os.path.join(images_dir, f))]

# Shuffle and split
random.shuffle(image_files)
split_ratio = 0.8
split_index = int(len(image_files) * split_ratio)
train_images = image_files[:split_index]
val_images = image_files[split_index:]

def move_pair(img_list, img_dest, label_dest):
    for img_name in img_list:
        label_name = os.path.splitext(img_name)[0] + ".txt"

        # Full paths
        src_img = os.path.join(images_dir, img_name)
        src_lbl = os.path.join(labels_dir, label_name)

        dst_img = os.path.join(img_dest, img_name)
        dst_lbl = os.path.join(label_dest, label_name)

        # Move only if both image and label exist
        if os.path.exists(src_img) and os.path.exists(src_lbl):
            shutil.move(src_img, dst_img)
            shutil.move(src_lbl, dst_lbl)

# Move training and validation files
move_pair(train_images, image_train_dir, label_train_dir)
move_pair(val_images, image_val_dir, label_val_dir)

print(f"✅ Done! Moved {len(train_images)} to train/ and {len(val_images)} to val/")

