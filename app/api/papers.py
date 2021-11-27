from fastapi import APIRouter
from fastapi import HTTPException
from app.api.models import Paper
from typing import List


papers = APIRouter()


fake_paper_db = [
    {
        'author': 'James Freeman',
        'topic': 'Female nutrition',
        'content': 'Female nutrition sucks',
        'tags': ['female', 'nutrition', 'food'],
    }
]


@papers.get('/', response_model=List[Paper])
async def index():
    return fake_paper_db


@papers.post('/', status_code=201)
async def add(paper: Paper):
    paper = paper.dict()
    fake_paper_db.append(paper)

    return {'id': len(fake_paper_db) - 1}


@papers.put('/')
async def update(paper_id: int, paper: Paper):
    paper = paper.dict()
    papers_quantity = len(fake_paper_db)

    if 0 <= paper_id < papers_quantity:
        fake_paper_db[paper_id] = paper
        return None

    raise HTTPException(
        status_code=400,
        detail='Paper with given id not found',
    )


@papers.delete('/')
async def delete(paper_id: int):
    papers_quantity = len(fake_paper_db)

    if 0 <= paper_id < papers_quantity:
        del fake_paper_db[paper_id]
        return None

    raise HTTPException(
        status_code=400,
        detail='Paper with given id not found',
    )
