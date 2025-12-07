import os
import shutil
import random
from pathlib import Path

def create_val_split(data_dir, val_ratio=0.1):
    """
    Take 10% from train to create validation set
    """
    
    print("\n" + "=" * 60)
    print("🔄 CREATING VALIDATION SPLIT")
    print("=" * 60)
    
    train_images = f"{data_dir}/train/images"
    train_labels = f"{data_dir}/train/labels"
    val_images = f"{data_dir}/val/images"
    val_labels = f"{data_dir}/val/labels"
    
    # Create val folders if they don't exist
    Path(val_images).mkdir(parents=True, exist_ok=True)
    Path(val_labels).mkdir(parents=True, exist_ok=True)
    
    # Get all training images
    all_images = [f for f in os.listdir(train_images) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    # Shuffle and select 10%
    random.shuffle(all_images)
    val_count = int(len(all_images) * val_ratio)
    val_images_list = all_images[:val_count]
    
    print(f"\n📊 Moving images to validation set:")
    print(f"  Total train images: {len(all_images)}")
    print(f"  Moving to val: {val_count} images")
    print(f"  Remaining in train: {len(all_images) - val_count} images")
    
    # Move images and labels
    moved = 0
    for img in val_images_list:
        # Get corresponding label filename
        label_name = img.rsplit('.', 1)[0] + '.txt'
        
        # Move image
        src_img = os.path.join(train_images, img)
        dst_img = os.path.join(val_images, img)
        shutil.move(src_img, dst_img)
        
        # Move label
        src_label = os.path.join(train_labels, label_name)
        dst_label = os.path.join(val_labels, label_name)
        if os.path.exists(src_label):
            shutil.move(src_label, dst_label)
        
        moved += 1
    
    print(f"\n✅ Moved {moved} image-label pairs to validation")
    
    # Verify
    final_train = len(os.listdir(train_images))
    final_val = len(os.listdir(val_images))
    
    print(f"\n📊 Final counts:")
    print(f"  train: {final_train} images")
    print(f"  val: {final_val} images")
    print(f"  test: {len(os.listdir(f'{data_dir}/test/images'))} images")
    print("=" * 60)

if __name__ == "__main__":
    create_val_split('data/combined_dataset')
