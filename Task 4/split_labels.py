import os

# Update these paths as per your structure
labels_txt_path = "labels.txt"
output_folder = "labels/train"  # or labels/val

os.makedirs(output_folder, exist_ok=True)

with open(labels_txt_path, "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) < 6:
            continue  # skip invalid lines
        image_file = parts[0]  # e.g., img1.jpg
        label_data = parts[1:] # class and box data

        txt_filename = os.path.splitext(image_file)[0] + ".txt"
        txt_path = os.path.join(output_folder, txt_filename)

        with open(txt_path, "a") as out_file:
            out_file.write(" ".join(label_data) + "\n")

print("✅ Done: Split labels into individual .txt files.")

