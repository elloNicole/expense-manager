from pydantic import BaseModel, Field
from typing import Optional

class ExpenseCreate(BaseModel):
    valor: float = Field(gt=0, description="O valor deve ser maior que zero")
    categoria: str
    data: str
    tipo: str = Field(pattern="^(entrada|saida)$")
    descricao: Optional[str] = None

class ExpenseResponse(ExpenseCreate):
    id: int
    
    class Config:
        from_attributes = True