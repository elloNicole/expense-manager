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

[![Interface do Projeto](/docs/image.png)]((https://www.figma.com/make/ggMZi8n2mQFcoKLCJenEsW/Untitled?fullscreen=1&t=09N1zCfbflbMWP28-1))

> 💡 **Dica:** Clique na imagem acima para acessar o protótipo interativo no Figma.

* **Baixa Fidelidade:** Esboços iniciais focados no fluxo do usuário: *Entrada de Dados -> Processamento -> Visualização de Tendência*.
* **Hierarquia de Informação:** Dados macro (Saldos totais) posicionados no topo, seguidos por dados analíticos (Gráficos) e, por fim, dados granulares (Tabela de extrato).
* **Paleta de Cores Funcional:** Utilização de cores semânticas via Tailwind CSS (ex: `text-emerald-500` para entradas e `text-rose-500` para saídas) para reduzir a carga cognitiva na interpretação dos dados.

---

## 📊 Requisitos e Processos

### Requisitos Funcionais (RF)
- **RF-01:** O sistema deve realizar o CRUD (Create, Read, Update, Delete) de transações financeiras.
- **RF-02:** O dashboard deve processar o saldo geral acumulado e os totais de entradas/saídas baseados no período selecionado.
- **RF-03:** O sistema deve plotar um gráfico de evolução diária que respeite o intervalo de datas definido pelo usuário.
- **RF-04:** O sistema deve calcular a variação percentual de gastos comparando o período atual com o anterior.

### Requisitos Não Funcionais (RNF)
- **RNF-01:** Persistência de dados e integridade referencial via banco de dados.
- **RNF-02:** Interface Single Page (SPI) onde a filtragem não exige novos reloads de página.
- **RNF-03:** Tratamento de objetos `Date` para evitar inconsistências de fuso horário no armazenamento.

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