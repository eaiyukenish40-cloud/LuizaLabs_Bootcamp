from controllers import post
from fastapi import FastAPI
import sqlalchemy as sa
import databases
from context

metadata = sqlalchemy.MetaData()
DATABASE_URL = "sqlite:///./blog.db"

engine = sa.create_engine(DATABASE_URL,
                          connect_args={"check_same_thread":False})

metadata.create_all(engine)

app = FastAPI()
app.include_router(post.router)
