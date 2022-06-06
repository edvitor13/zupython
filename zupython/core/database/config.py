from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    future=True,
    connect_args={"check_same_thread": False}
)

# connect_args={"check_same_thread": False}
# ...is needed only for SQLite. It's not needed for other databases.

SessionLocal: Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine
)

Base = declarative_base()

class Repository(Session):

    def __init__(self, *args, **kwargs):
        super().__init__(
            autocommit=False, 
            autoflush=False, 
            expire_on_commit=False,
            bind=engine
        )

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback) -> None:
        self.flush()
        self.commit()
        self.close()
        return super().__exit__(type_, value, traceback)
