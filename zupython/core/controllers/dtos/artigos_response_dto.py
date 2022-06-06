from pydantic import BaseModel

from .artigo_titulo_response_dto import ArtigoTituloResponseDto


class ArtigosResponseDto(BaseModel):
    total: int
    artigos: list[ArtigoTituloResponseDto]

    class Config:
        orm_mode = True
