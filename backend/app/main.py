import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from app.database.db import engine, Base
from app.routes import expense_routes


app = FastAPI(title="Expense Manager API")

# Criar banco
Base.metadata.create_all(bind=engine)

# Rotas
app.include_router(expense_routes.router)

@app.get("/")
def root():
    return {"message": "API rodando 🚀"}