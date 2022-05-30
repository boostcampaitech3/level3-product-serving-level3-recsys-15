from pydantic import BaseModel, Field
from typing import List

class Book(BaseModel):
    id: int
    title: str
    author: str
    img_url: str
    intro: str

class BookList(BaseModel):
    books: List[Book]=Field(default_factory=list)

class Music(BaseModel):
    id: int
    title: str
    artist: str
    url: str=Field(default_factory=str)

class MusicList(BaseModel):
    musics: List[Music]=Field(default_factory=list)