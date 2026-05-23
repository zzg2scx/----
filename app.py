from fastapi import FastAPI
from pydantic import BaseModel

from model.translator import translate_text

app = FastAPI()

# 请求数据结构
class TranslateRequest(BaseModel):
    text: str

# 首页接口
@app.get("/")
def home():
    return {
        "message": "壮语 AI 智能翻译系统运行成功"
    }

# 翻译接口
@app.post("/translate")
def translate(req: TranslateRequest):

    result = translate_text(req.text)

    return {
        "input": req.text,
        "translation": result
    }