import torch
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Model
model = torch.hub.load('ultralytics/yolov5','custom', path='best8.pt', force_reload=True)

# Images
imgs = ['C:\Users\Dell\Downloads\sdamcp\wt_cp\Unfazed_Roads\images\phone.png']  # batch of images

# Inference
results = model(imgs)

# Results
results.print()
results.save()  # or .show()

results.xyxy[0]  # img1 predictions (tensor)
results.pandas().xyxy[0]