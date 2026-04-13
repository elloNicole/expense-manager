from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.database.db import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float, nullable=False)
    categoria = Column(String, nullable=False)
    data = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)