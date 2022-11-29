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


@app.post("/predict/")
def predict(source: SourceText):
    """Генерация текста"""
    result_text = generator(source.text, max_length=source.len)
    return {"generated_text": result_text[0]['generated_text']}
