from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):
    valor: float = Field(gt=0)
    categoria: str
    data: str
    descricao: str | None = None

class ExpenseResponse(BaseModel):
    id: int
    valor: float
    categoria: str
    data: str
    descricao: str | None

    class Config:
        from_attributes = True