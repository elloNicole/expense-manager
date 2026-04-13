from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from typing import List
import sqlite3
import os
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CONFIGURAÇÃO DE CAMINHOS ---
# 1. Onde este arquivo (main.py) está: .../backend/app/
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Volta um nível para: .../backend/
BACKEND_DIR = os.path.dirname(CURRENT_DIR)

# 3. Volta mais um nível para a raiz do projeto: .../expense-maneger/
ROOT_DIR = os.path.dirname(BACKEND_DIR)

# Caminho do Front-end (está dentro da pasta raiz, em "frontend/static")
STATIC_PATH = os.path.join(ROOT_DIR, "frontend", "static")

# Caminho do Banco de Dados
DB_PATH = os.path.join(BACKEND_DIR, "expenses.db")
# --------------------------------
# Monta a pasta do Front-end
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(STATIC_PATH, "index.html"))

class Expense(BaseModel):
    id: int = None
    descricao: str = Field(..., min_length=2, max_length=50)
    valor: float = Field(..., gt=0)
    data: str 
    categoria: str = Field(..., min_length=2)
    tipo: str = Field(..., pattern="^(entrada|saida)$")

    @field_validator('data')
    @classmethod
    def validate_date(cls, v):
        try:
            dt = datetime.strptime(v, '%Y-%m-%d')
            if dt.year > 2100 or dt.year < 1900:
                raise ValueError("Ano fora do limite")
            return v
        except ValueError:
            raise HTTPException(status_code=400, detail="Data inválida no servidor")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.on_event("startup")
def setup_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS expenses 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  descricao TEXT, valor REAL, data TEXT, 
                  categoria TEXT, tipo TEXT)''')
    conn.commit()
    conn.close()

@app.get("/despesas", response_model=List[Expense])
def get_expenses():
    try:
        conn = get_db_connection()
        rows = conn.execute('SELECT * FROM expenses ORDER BY data DESC').fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except sqlite3.OperationalError:
        # Se por acaso a tabela ainda não existir no momento do get, retorna lista vazia
        return []

@app.post("/despesas")
def create_expense(exp: Expense):
    conn = get_db_connection()
    cursor = conn.execute(
        'INSERT INTO expenses (descricao, valor, data, categoria, tipo) VALUES (?, ?, ?, ?, ?)',
        (exp.descricao, exp.valor, exp.data, exp.categoria, exp.tipo)
    )
    conn.commit()
    conn.close()
    return {"id": cursor.lastrowid}

@app.delete("/despesas/{id}")
def delete_expense(id: int):
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return {"status": "ok"}