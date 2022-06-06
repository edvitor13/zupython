from ..entities.artigo import Artigo
from ..clients.articles_client import ArticlesClient
from ..controllers.mappers.artigo_mapper import ArtigoMapper
from ..repositories.artigo_repository import ArtigoRepository


class ArtigoService:
    
    @staticmethod
    def obter_por_autor_client(autor: str) -> list[Artigo]:
        return ArtigoMapper.artigos_para_entidade(
            ArticlesClient.obter_por_autor(autor)
        )


    @staticmethod
    def salvar_artigos(artigos: list[Artigo]) -> list[Artigo]:
        with ArtigoRepository() as ar:
            for artigo in artigos:
                if (not ArtigoRepository.existe(artigo)):
                    ar.add(artigo)
        
        return artigos


    @staticmethod
    def obter_e_salvar(autor: str) -> list[Artigo]:
        artigos: list[Artigo] = ArtigoService.obter_por_autor_client(autor)
        artigos = list(filter(lambda a: a.titulo is not None, artigos))

        return ArtigoService.salvar_artigos(artigos)
