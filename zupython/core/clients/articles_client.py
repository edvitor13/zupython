import requests

from .dtos.artigos_dto import ArtigosDto


class ArticlesClient:
    URL: str = "https://jsonmock.hackerrank.com/api/articles"
    
    @staticmethod
    def obter_por_autor(author: str) -> ArtigosDto:
        try:
            resp = requests.get(url=ArticlesClient.URL, params={
                "author": author
            })
            return ArtigosDto.parse_obj(resp.json())
        except:
            return ArtigosDto()
