import os

# Full path to your "labels" folder
label_dir = "/Users/dhanviannam/Documents/IIIT H proj/Task 4/dataset/labels"
subdirs = ["train", "val", "test"]

class_ids = set()

for subdir in subdirs:
    path = os.path.join(label_dir, subdir)
    if not os.path.exists(path):
        print(f"⚠️ Folder not found: {path}")
        continue

    for file in os.listdir(path):
        if file.endswith(".txt"):
            with open(os.path.join(path, file), "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if parts:
                        class_ids.add(int(parts[0]))

print(f"✅ Found {len(class_ids)} unique class IDs:")
print("Class IDs used:", sorted(class_ids))

