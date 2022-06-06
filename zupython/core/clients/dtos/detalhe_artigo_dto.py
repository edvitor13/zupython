from typing import Optional
from pydantic import BaseModel


class DetalheArtigoDto(BaseModel):
    title: Optional[str]
    url: Optional[str]
    author: Optional[str]
    num_comments: Optional[int]
    story_id: Optional[int]
    story_title: Optional[str]
    story_url: Optional[str]
    parent_id: Optional[int]
    created_at: Optional[int]

    def has_title(self) -> bool:
        return self.title is not None and len(self.title.strip()) > 0

    
    def has_story_title(self) -> bool:
        return self.story_title is not None \
            and len(self.story_title.strip()) > 0
