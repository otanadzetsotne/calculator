from app.api.models import PaperIn
from app.api.db import papers, database


async def get_paper(paper_id: int):
    query = papers.select(papers.c.id == paper_id)
    response = await database.fetch_one(query=query)

    return response


async def get_all_papers():
    query = papers.select()
    response = await database.fetch_all(query=query)

    return response


async def add_paper(paper: PaperIn):
    query = papers.insert().values(**paper.dict())
    response = await database.execute(query=query)

    return response


async def update_paper(paper_id: int, paper: PaperIn):
    query = papers.update().where(papers.c.id == paper_id).values(**paper.dict())
    response = await database.execute(query=query)

    return response


async def delete_paper(paper_id: int):
    query = papers.delete().where(papers.c.id == paper_id)
    response = await database.execute(query=query)

    return response
