from pydantic import BaseModel


class SourceTextLen(BaseModel):
    text: str
    text_len: int


class SourceText(BaseModel):
    text: str
