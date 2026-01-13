from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.db.base import Base


class ConteudoChunk(Base):
    __tablename__ = "conteudo_chunks"

    id = Column(Integer, primary_key=True, index=True)
    conteudo_id = Column(Integer, ForeignKey("conteudos.id"))
    texto = Column(Text, nullable=False)

    # embedding como array de floats serializado
    embedding = Column(Text, nullable=True)

    conteudo = relationship("Conteudo", back_populates="chunks")
