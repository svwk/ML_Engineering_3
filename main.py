from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()
generator = pipeline("text-generation", "gpt2")


class SourceTextLen(BaseModel):
    text: str
    textLen: int


class SourceText(BaseModel):
    text: str


@app.get("/")
async def root():
    return {"message": "Генерация текста"}


@app.post("/generateLen/")
def generateLen(source: SourceTextLen):
    """Генерация текста заданной длины"""
    result_text = generator(source.text, max_length=source.textLen)
    return {"generated_text": result_text[0]['generated_text']}


@app.post("/generate100/")
def generate100(source: SourceText):
    """Генерация текста фиксированной длины"""
    result_text = generator(source.text, max_length=100)
    return {"generated_text": result_text[0]['generated_text']}
