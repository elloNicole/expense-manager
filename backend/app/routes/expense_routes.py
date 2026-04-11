from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.schemas.expense_schema import ExpenseCreate, ExpenseResponse
from app.services import expense_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/despesas", response_model=ExpenseResponse)
def create(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return expense_service.create_expense(db, expense)

@router.get("/despesas")
def list_all(db: Session = Depends(get_db)):
    return expense_service.get_expenses(db)

@router.delete("/despesas/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return expense_service.delete_expense(db, id)

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    return expense_service.get_dashboard(db)

@router.get("/insights")
def insights(db: Session = Depends(get_db)):
    return expense_service.get_insights(db)