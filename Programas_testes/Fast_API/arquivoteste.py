from datetime import UTC, datetime
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {"título": "meu nome é panda", "data": datetime.now(UTC),"published": True},
    {"título": "meu nome é jamaica", "data": datetime.now(UTC),"published": True},
    {"título": "meu nome é panda", "data": datetime.now(UTC),"published": False},
]

class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False


@app.get("/")  # endpoint principal. Rota raíz
def home():
    return {"mensagem": "EU ESTOU RODANDO O CÓDIGO NOVO!"}

@app.post("/post/")
def create_post(post: Post):
    pass


# ROTA 2: A Rota Dinâmica
@app.get("/posts/{framework}")
def ler_posts(framework: str):
    return {"titulo": f"Artigo sobre {framework}", "status": "Funcionou"}



@app.get("/posts/{framework}/complementos")
def post_adicionais(published: bool, skip: int = 0, limit: int ):
    return [post for post in fake_db[skip : skip + limit] if post["published"] is published]
