from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import settings

URL_DATABASE = 'postgresql://postgres:postgres@5432:5432/postgres'

engine = create_engine(settings.postgres_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
