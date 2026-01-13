from sqlalchemy.orm import Session

from app.ai.chunking import split_text_into_chunks
from app.models.conteudo_chunk import ConteudoChunk


def processar_conteudo(db: Session, conteudo):
    chunks = split_text_into_chunks(conteudo.texto)

    for texto_chunk in chunks:
        chunk = ConteudoChunk(
            conteudo_id=conteudo.id,
            texto=texto_chunk
        )
        db.add(chunk)

    db.commit()

    print(f"{len(chunks)} chunks salvos para o conteúdo {conteudo.id}")