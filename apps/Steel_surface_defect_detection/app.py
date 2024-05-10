from fastapi import APIRouter
from typing import List

from fastapi import Form, File, UploadFile
from ultralytics import YOLO
from io import BytesIO
import numpy as np
import cv2
import os

app_detection = APIRouter()


@app_detection.post("/file")
async def get_file(file: bytes = File()):
    # 适合小文件上传
    print("file", file)
    return {
        "file": len(file)
    }


@app_detection.post("/files")
async def get_files(files: List[bytes] = File()):
    # 适合小文件上传
    # print("file", files)
    for file in files:
        print(len(file))
    return {
        "file": len(files)
    }


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

@app_detection.post("/uploadFile")
async def get_file(file: UploadFile):
    # 适合大文件上传
    contents = await file.read()
    result_list, conf_list= detect_img(contents)
    print(result_list)
    print(conf_list)
    return {
        "file": file.filename,
        "detection_result": result_list,
        "conf_list": conf_list
    }



@app_detection.post("/uploadFiles")
async def getUploadFiles(files: List[UploadFile]):
    # 适合大文件上传
    print("file", files)

    return {
        "names": [file.filename for file in files]
    }
