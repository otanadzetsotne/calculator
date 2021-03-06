from fastapi import FastAPI
from app.api.papers import papers
from app.api.db import metadata, database, engine


metadata.create_all(engine)


app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(papers, prefix='/api/papers', tags=['movies'])
