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

    @staticmethod
    def obter(author: str, page: int, per_page: int) -> ArtigosDto:
        try:
            resp = requests.get(url=ArticlesClient.URL, params={
                "author": author,
                "page": page,
                "per_page": per_page
            })
            return ArtigosDto.parse_obj(resp.json())
        except:
            return ArtigosDto()
