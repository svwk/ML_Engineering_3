from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()
generator = pipeline("text-generation", "gpt2")


class SourceText(BaseModel):
    text: str
    len: int


@app.get("/")
async def root():
    return {"message": "Генерация текста"}


@app.post("/generateLen/")
def predict(source: SourceText):
    """Генерация текста заданной длины"""
    result_text = generator(source.text, max_length=source.len)
    return {"generated_text": result_text[0]['generated_text']}


@app.post("/generate100/")
def predict(text: str):
    """Генерация текста фиксированной длины"""
    result_text = generator(text, max_length=100)
    return {"generated_text": result_text[0]['generated_text']}
