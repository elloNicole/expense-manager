from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho do banco SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./expenses.db"

# O echo=True ajuda você a ver o SQL no terminal (bom para debug)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função para obter o DB nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()