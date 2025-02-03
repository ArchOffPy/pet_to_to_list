from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Теперь импортируем Base из models.py

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)  # Создание таблиц

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
