A solução segue o modelo de arquitetura **Cliente-Servidor** desacoplada, garantindo independência entre as camadas.

### Componentes Principais:
1.  **Camada de Persistência:** Banco de dados relacional gerenciado via **SQLAlchemy**, garantindo a tipagem e integridade dos registros financeiros.
2.  **Camada de Aplicação (API):** Desenvolvida em **FastAPI**, utilizando modelos Pydantic para validação de esquemas JSON no tráfego de dados.
3.  **Camada de Apresentação:** SPA (Single Page Application) construída com JavaScript Vanilla, utilizando a técnica de manipulação de estado local para filtragem de arrays de alta performance.

### Modelo de Dados (Entidade-Relacionamento):
* **Transação:** * `id` (Primary Key)
    * `descricao` (String)
    * `valor` (Float/Numeric)
    * `data` (Date)
    * `categoria` (String)
    * `tipo` (Enum: Entrada/Saida)