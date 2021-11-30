from typing import List, Optional
from pydantic import BaseModel


class Paper(BaseModel):
    author: str
    topic: str
    content: str
    tags: List[str]


class PaperIn(Paper):
    pass


class PaperOut(Paper):
    id: int


class PaperUpdate(Paper):
    author: Optional[str] = None
    topic: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None
