from typing import List

from fastapi import APIRouter
from fastapi import HTTPException

from app.api.models import Paper, PaperIn, PaperOut, PaperUpdate
from app.api import db_manager


papers = APIRouter()


@papers.get('/', response_model=List[PaperOut])
async def index():
    return await db_manager.get_all_papers()


@papers.post('/', status_code=201, response_model=PaperOut)
async def add(payload: PaperIn):
    paper_id = await db_manager.add_paper(payload)

    return PaperOut(
        id=paper_id,
        **payload.dict(),
    )


@papers.put('/{id}')
async def update(paper_id: int, payload: PaperUpdate):
    paper = await db_manager.get_paper(paper_id)

    if not paper:
        raise HTTPException(
            status_code=400,
            detail='Paper with given id not found',
        )

    data = payload.dict(exclude_unset=True)
    paper_in_db = PaperIn(**paper)
    paper_updated = paper_in_db.copy(update=data)
    return await db_manager.update_paper(paper_id, paper_updated)


@papers.delete('/{id}')
async def delete(paper_id: int):
    paper = await db_manager.get_paper(paper_id)

    if not paper:
        raise HTTPException(
            status_code=400,
            detail='Paper with given id not found',
        )

    return await db_manager.delete_paper(paper_id)
