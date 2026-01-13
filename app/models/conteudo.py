from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base import Base


class Conteudo(Base):
    __tablename__ = "conteudos"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(255), nullable=False)
    texto = Column(Text, nullable=False)

    chunks = relationship(
        "ConteudoChunk",
        back_populates="conteudo",
        cascade="all, delete-orphan"
    )