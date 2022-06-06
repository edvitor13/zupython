from pydantic import BaseModel


class ArtigoTituloResponseDto(BaseModel):
    titulo: str

    class Config:
        orm_mode = True
