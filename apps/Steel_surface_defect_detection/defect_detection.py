import numpy as np
import cv2
from ultralytics import YOLO
def detect_img(contents):
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Load a pretrained YOLOv8n model
    model = YOLO('trained/weights/best_gc.pt')
    # Run inference on 'bus.jpg' with arguments
    pred = model.predict(source=img, save=True, imgsz=640, conf=0.25)
    cls_list_int = [int(i) for i in pred[0].boxes.cls.tolist()]
    class_names = ["crazing", "inclusion", "patches", "pitted_surface", "rolled-in_scale", "scratches"]
    result_list = [class_names[i] for i in cls_list_int]
    conf_list = pred[0].boxes.conf.tolist()
    return result_list,conf_list