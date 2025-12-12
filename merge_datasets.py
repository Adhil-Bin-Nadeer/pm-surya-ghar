import os
import shutil
from pathlib import Path

def merge_datasets(source_dirs, output_dir):
    """Merge multiple datasets into one"""
    
    print("=" * 60)
    print("🔀 MERGING DATASETS")
    print("=" * 60)
    
    # Create output directories
    splits = ['train', 'val', 'test']
    for split in splits:
        Path(f"{output_dir}/{split}/images").mkdir(parents=True, exist_ok=True)
        Path(f"{output_dir}/{split}/labels").mkdir(parents=True, exist_ok=True)
    
    total_images = 0
    total_labels = 0
    
    # Process each source
    for idx, source_dir in enumerate(source_dirs, 1):
        print(f"\n📂 Processing Source {idx}: {source_dir}")
        
        for split in splits:
            # Source paths
            src_images = f"{source_dir}/{split}/images"
            src_labels = f"{source_dir}/{split}/labels"
            
            # Destination paths
            dst_images = f"{output_dir}/{split}/images"
            dst_labels = f"{output_dir}/{split}/labels"
            
            # Copy images
            if os.path.exists(src_images):
                img_count = 0
                for img in os.listdir(src_images):
                    src_file = os.path.join(src_images, img)
                    dst_file = os.path.join(dst_images, img)
                    if os.path.isfile(src_file):
                        shutil.copy2(src_file, dst_file)
                        img_count += 1
                        total_images += 1
                if img_count > 0:
                    print(f"   ✅ {split}: {img_count} images copied")
            
            # Copy labels
            if os.path.exists(src_labels):
                lbl_count = 0
                for label in os.listdir(src_labels):
                    src_file = os.path.join(src_labels, label)
                    dst_file = os.path.join(dst_labels, label)
                    if os.path.isfile(src_file):
                        shutil.copy2(src_file, dst_file)
                        lbl_count += 1
                        total_labels += 1
                if lbl_count > 0:
                    print(f"   ✅ {split}: {lbl_count} labels copied")
    
    print("\n" + "=" * 60)
    print("✅ MERGE COMPLETE!")
    print("=" * 60)
    print(f"Total images copied: {total_images}")
    print(f"Total labels copied: {total_labels}")
    
    # Count by split
    print("\n📊 Final counts:")
    for split in splits:
        images_path = f"{output_dir}/{split}/images"
        if os.path.exists(images_path):
            count = len([f for f in os.listdir(images_path) if f.endswith(('.jpg', '.png', '.jpeg'))])
            print(f"  {split}: {count} images")
    
    return total_images

# Run
if __name__ == "__main__":
    source_dirs = [
        'data/source1_alfred_weber',
        'data/source2_lsgi547',
        'data/source3_piscinas'
    ]
    
    output_dir = 'data/combined_dataset'
    
    merge_datasets(source_dirs, output_dir)
