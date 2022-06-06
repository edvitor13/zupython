from fastapi import APIRouter

from ..services.artigo_service import ArtigoService
from ..controllers.mappers.artigo_mapper import ArtigoMapper
from ..controllers.dtos.artigos_response_dto import ArtigosResponseDto


router = APIRouter(prefix="/artigos/importador", tags=["artigos"])


@router.post(
    "/",
    response_model=ArtigosResponseDto,
    summary="Artigos Hackerrank"
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
