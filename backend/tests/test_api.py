from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# TESTE 1: GET vazio
def test_get_empty_expenses():
    response = client.get("/despesas")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# TESTE 2: Criar despesa
def test_create_expense():
    response = client.post("/despesas", json={
        "descricao": "Teste mercado",
        "valor": 100.0,
        "data": "2024-04-10",
        "categoria": "Alimentação",
        "tipo": "saida"
    })

    assert response.status_code == 200
    assert "id" in response.json()


# TESTE 3: Criar inválido (valor negativo)
def test_create_invalid_expense():
    response = client.post("/despesas", json={
        "descricao": "Erro",
        "valor": -50,
        "data": "2024-04-10",
        "categoria": "Teste",
        "tipo": "saida"
    })

    assert response.status_code == 422


# TESTE 4: Data inválida
def test_invalid_date():
    response = client.post("/despesas", json={
        "descricao": "Teste",
        "valor": 100,
        "data": "3000-01-01",  # fora do limite
        "categoria": "Teste",
        "tipo": "saida"
    })

    assert response.status_code == 400


# TESTE 5: Deletar despesa
def test_delete_expense():
    # cria primeiro
    create = client.post("/despesas", json={
        "descricao": "Para deletar",
        "valor": 50,
        "data": "2024-04-10",
        "categoria": "Teste",
        "tipo": "saida"
    })

    expense_id = create.json()["id"]

    # deleta
    response = client.delete(f"/despesas/{expense_id}")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"