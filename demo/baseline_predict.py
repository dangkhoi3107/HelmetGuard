from ultralytics import YOLO
import sys

"""
Baseline demo:
- Uses pretrained YOLOv8n (COCO) to prove the pipeline runs.
- After fine-tuning, replace with: runs/detect/train/weights/best.pt

Usage:
  python demo/baseline_predict.py path/to/image_or_folder
"""

source = sys.argv[1] if len(sys.argv) > 1 else "assets"
model = YOLO("yolov8n.pt")
model.predict(source=source, conf=0.25, save=True)
print("Saved outputs to runs/detect/predict/")
