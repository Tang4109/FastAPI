from fastapi import APIRouter,Depends
from fastapi import Form, File, UploadFile
from typing import Union, Optional, List
from pydantic import BaseModel, Field, validator
from datetime import date
from typing import List
import torch
from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)
from .query_answer import QA
app_LLM = APIRouter()

# 单例模式来确保模型只加载一次,单例模式确保类只有一个实例
class ModelManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load_model()
        return cls._instance

    def load_model(self):
        # 这里加载模型的代码
        model_dir = "C:/Users/LOGAN/.cache/modelscope/hub/LLM-Research/Phi-3-mini-128k-instruct"
        self.model = AutoModelForCausalLM.from_pretrained(
            model_dir,
            device_map="cuda",
            torch_dtype="auto",
            trust_remote_code=True,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)

    def get_model(self):
        return self.model

    def get_tokenizer(self):
        return self.tokenizer


def get_model_manager():
    return ModelManager()

def get_qa_instance(model_manager: ModelManager = Depends(get_model_manager)):
    return QA(model_manager)

# 请求体数据
class Query(BaseModel):
    role: str = "user"
    content: str
@app_LLM.post("/query")
async def query(query: Query,qa_instance: QA  = Depends(get_qa_instance)):
    answer = qa_instance(query.role, query.content)
    return answer

