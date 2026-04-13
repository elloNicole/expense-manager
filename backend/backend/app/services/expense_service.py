from sqlalchemy.orm import Session
from app.models.expense import Expense

def create_expense(db: Session, expense_data):
    expense = Expense(**expense_data.dict())
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

    total = sum(e.valor for e in expenses)

    categorias = {}
    for e in expenses:
        categorias[e.categoria] = categorias.get(e.categoria, 0) + e.valor

    return {
        "total_gasto": total,
        "gasto_por_categoria": categorias
    }

def get_insights(db: Session):
    expenses = db.query(Expense).all()

    if not expenses:
        return {"insight": "Sem dados suficientes"}

    categorias = {}
    for e in expenses:
        categorias[e.categoria] = categorias.get(e.categoria, 0) + e.valor

    maior_categoria = max(categorias, key=categorias.get)

    return {
        "maior_categoria": maior_categoria,
        "mensagem": f"Você gasta mais com {maior_categoria}"
    }