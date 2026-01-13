def split_text_into_chunks(
    texto: str,
    tamanho_maximo: int = 500,
    sobreposicao: int = 50
) -> list[str]:
    palavras = texto.split()
    chunks = []
    inicio = 0

    while inicio < len(palavras):
        fim = inicio + tamanho_maximo
        chunk = " ".join(palavras[inicio:fim])
        chunks.append(chunk)
        inicio += tamanho_maximo - sobreposicao

    return chunks