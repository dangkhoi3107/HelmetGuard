## Dataset (Roboflow Export)

This project uses a small self-labeled dataset exported from Roboflow in **YOLOv8** format.

Expected structure (not committed to Git):
dataset/
  data.yaml
  train/images, train/labels
  valid/images, valid/labels

How to reproduce:
1) Export dataset from Roboflow as "YOLOv8 PyTorch"
2) Unzip into this `dataset/` folder
