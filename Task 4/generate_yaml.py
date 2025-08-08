import os

# Adjust this path to your dataset root
dataset_root = "/Users/dhanviannam/Documents/IIIT H proj/Task 4/dataset"
labels_path = os.path.join(dataset_root, "labels")

class_ids = set()

# Scan train, val, test folders
for split in ["train", "val", "test"]:
    folder = os.path.join(labels_path, split)
    for fname in os.listdir(folder):
        if fname.endswith(".txt"):
            with open(os.path.join(folder, fname), "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if parts:
                        class_ids.add(int(parts[0]))

# Sort and create placeholder names
sorted_ids = sorted(class_ids)
names = [f"class{idx}" for idx in sorted_ids]

# Write data.yaml
yaml_path = os.path.join(dataset_root, "data.yaml")
with open(yaml_path, "w") as f:
    f.write(f"path: {dataset_root}\n\n")
    f.write("train: images/train\n")
    f.write("val: images/val\n\n")
    f.write(f"nc: {len(names)}\n")
    f.write("names:\n")
    for i, name in enumerate(names):
        f.write(f"  {i}: {name}\n")

print(f"✅ data.yaml created with {len(names)} classes at:")
print(f"   {yaml_path}")
