from pydantic import BaseModel

from .detalhe_artigo_dto import DetalheArtigoDto


class ArtigosDto(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[DetalheArtigoDto]
