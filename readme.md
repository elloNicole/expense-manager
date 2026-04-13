# Expense Manager

Aplicação full-stack para gerenciamento de fluxo de caixa pessoal, focada em análise de dados transacionais através de dashboard dinâmico.

## 🛠 Especificações Técnicas

### Backend
- **API:** FastAPI (Python) para alta performance e documentação automática (Swagger).
- **Persistência:** SQLAlchemy para mapeamento objeto-relacional (ORM).
- **Arquitetura:** Estruturação de rotas para operações CRUD de transações.

### Frontend
- **Interface:** Tailwind CSS para estilização baseada em utilitários e layout responsivo.
- **Visualização de Dados:** Chart.js para renderização de gráficos em tempo real.
- **Lógica de Estado:** Manipulação de DOM e filtragem de arrays via JavaScript (ES6) para atualização reativa dos componentes de UI.

---

## 🎨 Prototipação e UX

O design foi estruturado seguindo princípios de **Dashboarding**, onde a hierarquia visual prioriza a tomada de decisão rápida.

[![Interface do Projeto](/docs/image.png)](https://www.figma.com/make/ggMZi8n2mQFcoKLCJenEsW/Untitled?fullscreen=1&t=09N1zCfbflbMWP28-1)

> 💡 **Dica:** Clique no link para acessar o protótipo interativo no Figma: https://www.figma.com/make/ggMZi8n2mQFcoKLCJenEsW/Untitled?fullscreen=1&t=09N1zCfbflbMWP28-1.

* **Baixa Fidelidade:** Esboços iniciais focados no fluxo do usuário: *Entrada de Dados -> Processamento -> Visualização de Tendência*.
* **Hierarquia de Informação:** Dados macro (Saldos totais) posicionados no topo, seguidos por dados analíticos (Gráficos) e, por fim, dados granulares (Tabela de extrato).
* **Paleta de Cores Funcional:** Utilização de cores semânticas via Tailwind CSS (ex: `text-emerald-500` para entradas e `text-rose-500` para saídas) para reduzir a carga cognitiva na interpretação dos dados.

---

### 📋 Requisitos e Diretrizes Técnicas

#### Requisitos Funcionais (RF)
* **RF-01 (Persistência Transacional):** O sistema deve gerenciar o ciclo de vida completo (CRUD) de ativos financeiros, garantindo a integridade dos registros de entrada e saída.
* **RF-02 (Agregação de Dados):** O motor do dashboard deve processar o saldo líquido acumulado e os volumes de aporte/escoamento em conformidade com o subset de dados selecionado.
* **RF-03 (Telemetria Temporal):** Plotagem dinâmica de séries temporais (Time Series) para evolução diária, sincronizada estritamente com o intervalo cronológico definido pelo usuário.
* **RF-04 (Análise MoM):** Algoritmo de inteligência financeira para cálculo de variação percentual comparativa entre o período corrente e o histórico anterior (Month over Month).

#### Requisitos Não Funcionais (RNF)
* **RNF-01 (Integridade Referencial):** Persistência de dados robusta e garantia de relacionamentos via ORM (SQLAlchemy) em banco de dados relacional.
* **RNF-02 (Arquitetura SPA):** Interface de página única (Single Page Application) com manipulação de estado local, eliminando a necessidade de reloads para filtragem de dados.
* **RNF-03 (Normalização Temporal):** Tratamento rigoroso de objetos `Date` e sincronização de fuso horário (UTC/ISO 8601) para mitigar inconsistências no armazenamento e exibição.

---

## 🔄 Fluxo de Processamento de Dados

O fluxo de dados foi projetado para minimizar o overhead de requisições:

1. **Fetch Inicial:** O frontend carrega o set de dados completo via API.
2. **Filtragem por Período:** Uma função de processamento intercepta o array original e aplica filtros de data.
3. **Agregação:** Os dados filtrados passam por métodos de redução (`reduce`/`map`) para extrair os valores dos cards e os eixos dos gráficos.
4. **Renderização:** O método `Chart.update()` é invocado para re-renderizar os gráficos de linha (evolução) e rosca (categorias) com os novos subsets de dados.

---

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.x
- Navegador moderno com suporte a ES6

### Execução do Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn main:app --reload