from typing import Optional
from fastapi import APIRouter, status

from ..services.artigo_service import ArtigoService
from ..controllers.mappers.artigo_mapper import ArtigoMapper
from ..controllers.dtos.artigos_response_dto import ArtigosResponseDto
from ..clients.dtos.artigos_dto import ArtigosDto
from ..clients.articles_client import ArticlesClient


router = APIRouter(prefix="/artigos", tags=["artigos"])


@router.post(
    "/importador",
    response_model=ArtigosResponseDto,
    summary="Importa Artigos Hackerrank", 
    status_code=status.HTTP_201_CREATED
)
async def importa_artigos(autor: str):
    """
    1. Filtra os artigos (pelo autor) de "jsonmock.hackerrank.com/api/articles"

    2. Após filtrar, registra no banco local os títulos válidos e o autor

    3. Após registrar, exibe os títulos dos artigos e suas quantidades
    """
    return ArtigoMapper.entidades_para_artigos_response(
        ArtigoService.obter_e_salvar(autor)
    )


@router.get(
    "/client",
    response_model=ArtigosDto,
    summary="Exibe Artigos Diretamente da API da Hackerrank", 
    status_code=status.HTTP_200_OK
)
async def artigos(autor: Optional[str]=None, page: int=1, per_page: int=10):
    """
    Busca os artigos por autor e pagina
    """
    return ArticlesClient.obter(autor, page, per_page)
