from sqlalchemy import Column, Integer, String

from ..database import Base, engine


class Artigo(Base):
    __tablename__ = "artigos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    autor = Column(String)


Base.metadata.create_all(engine)
