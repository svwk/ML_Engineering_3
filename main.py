from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()
generator = pipeline("text-generation", "gpt2")


class SourceTextLen(BaseModel):
    text: str
    text_len: int


class SourceText(BaseModel):
    text: str


@app.get("/")
async def root():
    return {"message": "Генерация текста"}


@app.post("/generate_len/")
def generate_len(source: SourceTextLen):
    """Text generation using user input
    - **text**: input user text
    - **text_len**: count of output symbols
    """
    result_text = generator(source.text, max_length=source.text_len)
    return {"generated_text": result_text[0]['generated_text']}


@app.post("/generate_100/")
def generate_100(source: SourceText):
    """Text generation using text user input and const (100) value of symbols count
    - **text**: input user text
    """
    result_text = generator(source.text, max_length=100)
    return {"generated_text": result_text[0]['generated_text']}
