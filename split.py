import os
import random
import shutil

random.seed(42)

image_dir = r"E:\Helmet detection\dataset\images"
label_dir = r"E:\Helmet detection\dataset\labels"
output_base = r"E:\Helmet detection\dataset"

train_img_dir = os.path.join(output_base, "images/train")
val_img_dir = os.path.join(output_base, "images/val")
train_lbl_dir = os.path.join(output_base, "labels/train")
val_lbl_dir = os.path.join(output_base, "labels/val")

for d in [train_img_dir, val_img_dir, train_lbl_dir, val_lbl_dir]:
    os.makedirs(d, exist_ok=True)

image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(image_files)

split_index = int(len(image_files) * 0.8)
train_files = image_files[:split_index]
val_files = image_files[split_index:]

def copy_files(file_list, target_img_dir, target_lbl_dir):
    for fname in file_list:
        
        shutil.copy(os.path.join(image_dir, fname), os.path.join(target_img_dir, fname))
        
        label_file = fname.rsplit('.', 1)[0] + ".txt"
        src_label = os.path.join(label_dir, label_file)
        if os.path.exists(src_label):
            shutil.copy(src_label, os.path.join(target_lbl_dir, label_file))

copy_files(train_files, train_img_dir, train_lbl_dir)
copy_files(val_files, val_img_dir, val_lbl_dir)

print(f"Done: {len(train_files)} train images, {len(val_files)} val images.")
