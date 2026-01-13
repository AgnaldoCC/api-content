from app.ai.pipeline import processar_conteudo
from app.models.conteudo import Conteudo


class ConteudoService:

    @staticmethod
    def criar(db, dados):
        conteudo = Conteudo(
            titulo=dados.titulo,
            texto=dados.texto
        )

        db.add(conteudo)
        db.commit()
        db.refresh(conteudo)

        processar_conteudo(db, conteudo)

        return conteudo
