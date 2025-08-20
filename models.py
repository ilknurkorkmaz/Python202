from __future__ import annotations
from pydantic import BaseModel, Field, validator
from typing import List

class BookModel(BaseModel):
    title: str
    author: str
    isbn: str = Field(..., description="Unique ISBN identifier")

class IsbnIn(BaseModel):
    isbn: str

    @validator("isbn")
    def strip_isbn(cls, v: str) -> str:
        return v.replace("-", "").strip()