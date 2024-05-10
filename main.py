from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from apps.Steel_surface_defect_detection.app import app_detection

app = FastAPI()

# 静态文件
app.mount("/static", StaticFiles(directory="statics"))

app.include_router(app_detection, tags=["缺陷检测"])


if __name__ == '__main__':
    uvicorn.run("main:app", port=8090, reload=True)
