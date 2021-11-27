from fastapi import FastAPI
from app.api.papers import papers


app = FastAPI()
app.include_router(papers)
