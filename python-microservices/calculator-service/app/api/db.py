from databases import Database
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    ARRAY,
)

from app.api.configs import DATABASE_URI


metadata = MetaData()


papers = Table(
    'papers',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('author', String(255)),
    Column('topic', String(255)),
    Column('content', String),
    Column('tags_id', ARRAY(Integer)),
)

engine = create_engine(DATABASE_URI)
database = Database(DATABASE_URI)
