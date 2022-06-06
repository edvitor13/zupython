from ..database import Repository
from ..entities.artigo import Artigo


class ArtigoRepository(Repository):
    
    @staticmethod
    def existe(artigo: Artigo) -> bool:
        with ArtigoRepository() as ar:
            return bool(
                ar.query(Artigo)
                .filter(
                    (Artigo.titulo == artigo.titulo)
                    & (Artigo.autor == artigo.autor)
                )
                .limit(1)
                .count()
            )
