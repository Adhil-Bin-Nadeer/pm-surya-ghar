import os

print("\n" + "=" * 60)
print("✅ VERIFYING MERGE")
print("=" * 60)

# Check combined_dataset exists
if os.path.exists('data/combined_dataset'):
    print("✅ combined_dataset folder exists")
else:
    print("❌ combined_dataset folder NOT found")
    exit()

# Check data.yaml exists
if os.path.exists('data/combined_dataset/data.yaml'):
    print("✅ data.yaml exists")
else:
    print("❌ data.yaml NOT found")

# Count images
splits = ['train', 'val', 'test']
total = 0
for split in splits:
    path = f"data/combined_dataset/{split}/images"
    if os.path.exists(path):
        count = len([f for f in os.listdir(path) if f.endswith(('.jpg', '.png', '.jpeg'))])
        print(f"✅ {split}: {count} images")
        total += count
    else:
        print(f"❌ {split} folder NOT found")

print(f"\n📊 TOTAL IMAGES: {total}")
if total >= 600:
    print("✅ SUCCESS! Ready for training!")
else:
    print(f"⚠️ Expected 600+, found {total}")
print("=" * 60)
