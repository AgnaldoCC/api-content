from pydantic import BaseModel


class ConteudoCreate(BaseModel):
    titulo: str
    texto: str

class ConteudoResponse(BaseModel):
    id: int
    titulo: str

    class Config:
        from_attributes = True