import os
import glob
import shutil

# Path to your dataset folder
dataset_path = r"E:\Helmet detection\dataset"

image_dir = os.path.join(dataset_path, "images")
label_dir = os.path.join(dataset_path, "labels")

counter = 1

# Get all image files in "images"
image_files = sorted(glob.glob(os.path.join(image_dir, "*.*")))

for img_path in image_files:
    ext = os.path.splitext(img_path)[1]
    new_img_name = f"frame{counter}{ext.lower()}"
    new_img_path = os.path.join(image_dir, new_img_name)

    # Find matching label
    base_name = os.path.splitext(os.path.basename(img_path))[0]
    old_label_path = os.path.join(label_dir, base_name + ".txt")
    new_label_path = os.path.join(label_dir, f"frame{counter}.txt")

    # Rename image
    shutil.move(img_path, new_img_path)

    # Rename label if exists
    if os.path.exists(old_label_path):
        shutil.move(old_label_path, new_label_path)

    print(f"Renamed {os.path.basename(img_path)} → {new_img_name} (with label frame{counter}.txt)")
    counter += 1

print("\n✅ All frames and labels renamed sequentially as frame1, frame2, ...")
