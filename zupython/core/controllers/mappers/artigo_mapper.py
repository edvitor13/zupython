from typing import Optional
from ...entities.artigo import Artigo
from ...clients.dtos.artigos_dto import ArtigosDto
from ...clients.dtos.detalhe_artigo_dto import DetalheArtigoDto
from ...controllers.dtos.artigo_titulo_response_dto import ArtigoTituloResponseDto
from ...controllers.dtos.artigos_response_dto import ArtigosResponseDto


class ArtigoMapper:

    @staticmethod
    def detalhe_para_entidade(detalhe_artigo_dto: DetalheArtigoDto) -> Artigo:
        titulo: Optional[str] = None

        if (detalhe_artigo_dto.has_title()):
            titulo = detalhe_artigo_dto.title

        elif (detalhe_artigo_dto.has_story_title()):
            titulo = detalhe_artigo_dto.story_title

        return Artigo(titulo=titulo, autor=detalhe_artigo_dto.author)

    
    @staticmethod
    def artigos_para_entidade(artigos_dto: ArtigosDto) -> list[Artigo]:
        artigos: list[Artigo] = []

        for detalhe in artigos_dto.data:
            artigos.append(ArtigoMapper.detalhe_para_entidade(detalhe))

        return artigos

    
    @staticmethod
    def entidade_para_titulo_response(artigo: Artigo) -> ArtigoTituloResponseDto:
        return ArtigoTituloResponseDto(titulo=artigo.titulo)

    
    @staticmethod
    def entidades_para_artigos_response(artigos: list[Artigo]) -> ArtigosResponseDto:
        artigo_dto: ArtigosResponseDto = ArtigosResponseDto(
            total=0, artigos=[])

        for artigo in artigos:
            artigo_dto.artigos.append(
                ArtigoMapper.entidade_para_titulo_response(artigo)
            )

        artigo_dto.total = len(artigo_dto.artigos)

        return artigo_dto
