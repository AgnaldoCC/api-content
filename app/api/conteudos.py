from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.conteudo import Conteudo
from app.schemas.conteudo import ConteudoCreate, ConteudoResponse
from app.services.conteudo_service import ConteudoService

router = APIRouter()

@router.post("/", response_model=ConteudoResponse)
def criar_conteudo(dados: ConteudoCreate, db: Session = Depends(get_db)):
    return ConteudoService.criar(db, dados)




@router.get("/", response_model=List[ConteudoResponse])
def listar_conteudos(db: Session = Depends(get_db)):
    return db.query(Conteudo).all()