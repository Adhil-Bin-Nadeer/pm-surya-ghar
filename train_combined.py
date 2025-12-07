from ultralytics import YOLO
import torch

print("\n" + "=" * 60)
print("🚀 STARTING MODEL TRAINING")
print("=" * 60)
print(f"GPU Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
print("=" * 60 + "\n")

# Load YOLOv8 Medium model
model = YOLO('yolov8m.pt')

# Train on combined dataset
results = model.train(
    data='data/combined_dataset/data.yaml',
    epochs=100,
    imgsz=640,
    batch=32,
    lr0=0.001,
    lrf=0.01,
    patience=20,
    device='cpu',
    name='solar_v1_official',
    project='runs/detect',
    save=True,
    augment=True,
    plots=True
)

print("\n" + "=" * 60)
print("✅ TRAINING COMPLETE!")
print("=" * 60)
print(f"Best model saved at: runs/detect/solar_v1_official/weights/best.pt")
print("=" * 60 + "\n")
