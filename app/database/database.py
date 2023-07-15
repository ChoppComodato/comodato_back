from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ..utils import config


@lru_cache()
def get_settings():
    return config.Settings()

settings = get_settings()

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()