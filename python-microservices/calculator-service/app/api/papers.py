from typing import List

from fastapi import APIRouter
from fastapi import HTTPException

from app.api.models import PaperIn, PaperOut, PaperUpdate
from app.api import db_manager
from app.api.service import tag_exists


papers = APIRouter()


@papers.get('/', response_model=List[PaperOut])
async def get_all():
    return await db_manager.get_all_papers()


@papers.get('/{id}', response_model=PaperOut)
async def get(paper_id: int):
    paper = await db_manager.get_paper(paper_id)

    if not paper:
        raise HTTPException(
            status_code=404,
            detail='Paper not found',
        )

    return paper


@papers.post('/', status_code=201, response_model=PaperOut)
async def add(payload: PaperIn):
    for tag_id in payload.tags_id:
        if not tag_exists(tag_id):
            raise HTTPException(
                status_code=404,
                detail='Tag not found',
            )

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
            detail='Paper not found',
        )

    if payload.tags_id is not None:
        for tag_id in payload.tags_id:
            if not tag_exists(tag_id):
                raise HTTPException(
                    status_code=404,
                    detail='Tag not found',
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
            detail='Paper not found',
        )

    return await db_manager.delete_paper(paper_id)
