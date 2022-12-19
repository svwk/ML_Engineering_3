from fastapi import APIRouter


from models import SourceTextLen, SourceText
from utils import Utils

api_router = APIRouter()

@api_router.get("/")
async def root():
    return {"message": "Генерация текста"}


@api_router.post("/generate_len/")
def generate_len(source: SourceTextLen):
    """Text generation using user input
    - **text**: input user text
    - **text_len**: count of output symbols
    """
    generator = Utils()
    return generator.generate_text(source.text, source.text_len)


@api_router.post("/generate_100/")
def generate_100(source: SourceText):
    """Text generation using text user input and const (100) value of symbols count
    - **text**: input user text
    """
    generator = Utils()
    return generator.generate_text(source.text, 100)
