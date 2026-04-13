import pandas as pd
from sqlalchemy.orm import Session
from app.models.expense import Expense

def create_expense(db: Session, expense_data):
    # .dict() para Pydantic v1 ou .model_dump() para v2
    data = expense_data.dict() if hasattr(expense_data, 'dict') else expense_data.model_dump()
    expense = Expense(**data)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def get_expenses(db: Session):
    return db.query(Expense).all()

def delete_expense(db: Session, expense_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense:
        db.delete(expense)
        db.commit()
    return expense

def get_dashboard(db: Session):
    expenses = db.query(Expense).all()

    if not expenses:
        return {"total_entrada": 0, "total_saida": 0, "saldo": 0, "categorias": {}}

    # Criando DataFrame do Pandas
    df = pd.DataFrame([
        {"valor": e.valor, "tipo": e.tipo, "categoria": e.categoria} 
        for e in expenses
    ])

    # Cálculos com Pandas
    total_entrada = df[df['tipo'] == 'entrada']['valor'].sum()
    total_saida = df[df['tipo'] == 'saida']['valor'].sum()
    
    # Agrupamento por categoria (apenas das saídas)
    gastos_cat = df[df['tipo'] == 'saida'].groupby('categoria')['valor'].sum().to_dict()

    return {
        "total_entrada": float(total_entrada),
        "total_saida": float(total_saida),
        "saldo": float(total_entrada - total_saida),
        "gasto_por_categoria": gastos_cat
    }

def get_insights(db: Session):
    expenses = db.query(Expense).filter(Expense.tipo == "saida").all()

    if not expenses:
        return {"insight": "Sem dados de gastos para analisar."}

    df = pd.DataFrame([{"valor": e.valor, "categoria": e.categoria} for e in expenses])
    
    # Qual categoria tem a maior soma de valores?
    resumo = df.groupby('categoria')['valor'].sum()
    maior_categoria = resumo.idxmax()
    valor_maior = resumo.max()

    return {
        "maior_categoria": maior_categoria,
        "valor_total": float(valor_maior),
        "mensagem": f"Alerta: Sua maior fonte de gastos é {maior_categoria} (R$ {valor_maior:.2f})."
    }

def update_expense(db: Session, expense_id: int, data):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        return None

    update_data = data.dict() if hasattr(data, 'dict') else data.model_dump()
    
    for key, value in update_data.items():
        setattr(expense, key, value)

    db.commit()
    db.refresh(expense)
    return expense