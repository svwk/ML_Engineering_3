from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()
generator = pipeline("text-generation", "gpt2")


class SourceTextLen(BaseModel):
    """Input text"""
    text: str
    text_len: int


class SourceText(BaseModel):
    text: str


@app.get("/")
async def root():
    return {"message": "Генерация текста"}


@app.post("/generate_len/")
def generate_len(source: SourceTextLen):
    """Генерация текста заданной длины"""
    result_text = generator(source.text, max_length=source.text_len)
    return {"generated_text": result_text[0]['generated_text']}


@app.post("/generate_100/")
def generate_100(source: SourceText):
    """Генерация текста фиксированной длины"""
    result_text = generator(source.text, max_length=100)
    return {"generated_text": result_text[0]['generated_text']}
