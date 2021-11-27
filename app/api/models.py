from pydantic import BaseModel
from typing import List


class Paper(BaseModel):
    author: str
    topic: str
    content: str
    tags: List[str]
