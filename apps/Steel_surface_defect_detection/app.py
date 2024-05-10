from fastapi import APIRouter
from typing import List
from fastapi import Form, File, UploadFile
from io import BytesIO
import os
from .defect_detect import detect_img #.defect_detect 告诉 Python 在当前目录中查找 defect_detect 模块
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
