from fastapi import FastAPI

import app.db
from app.api import conteudos
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Assistente Inteligente de Estudos")

Base.metadata.create_all(bind=engine)

app.include_router(
    conteudos.router,
    prefix="/conteudos",
    tags=["Conteúdos"]
)

@app.get("/")
def healthcheck():
    return {"status": "ok"}
