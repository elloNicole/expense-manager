## 📋 Requisitos do Sistema

### Requisitos Funcionais (RF)
O conjunto de funcionalidades abaixo descreve as capacidades operacionais da aplicação:

* **RF-01 (Gestão de Transações):** O sistema deve implementar operações de CRUD para registros financeiros.
    * **Descrição:** Persistência de dados contendo descrição, valor (float), data (ISO 8601), categoria e metadado de tipo (entrada/saída).
    * **Validação:** Implementação de feedback visual diferenciado (Color Theory) para mitigar erros de input entre créditos e débitos.
* **RF-02 (Exclusão Segura):** O sistema deve permitir a remoção lógica e física de registros.
    * **Descrição:** Interface para expurgo de dados diretamente via componente de tabela.
    * **Validação:** Implementação de interceptação de evento (confirm prompt) para garantir a integridade da ação do usuário.
* **RF-03 (Dashboard Reativo):** Exibição de indicadores macrofinanceiros dinâmicos.
    * **Descrição:** Sumarização em tempo real de Saldo Líquido, Aporte Total e Escoamento Total.
    * **Validação:** Os componentes de KPI devem processar subsets de dados baseados nos filtros temporais ativos.
* **RF-04 (Visualização Analítica):** Renderização de telemetria financeira através de gráficos.
    * **Descrição:** Implementação de Gráfico de Linhas (Time Series) para evolução temporal e Gráfico de Barras/Rosca para distribuição categórica.
    * **Validação:** Os objetos de gráfico devem invocar métodos de re-renderização (`update`) sempre que o estado dos dados for alterado.
* **RF-05 (Inteligência Comparativa):** Cálculo de variação percentual (MoM - Month over Month).
    * **Descrição:** Algoritmo para comparar o volume de transações do período atual versus o período imediatamente anterior.
    * **Validação:** Tratamento de exceções para períodos sem histórico, evitando erros de divisão por zero ou dados nulos.
* **RF-06 (Filtragem de Ativos):** Motor de busca por intervalo cronológico.
    * **Descrição:** Seletores de data (Data Start/End) para segmentação granular do banco de dados.

### Requisitos Não Funcionais (RNF)
As restrições técnicas e qualidades sistêmicas que suportam a aplicação:

* **RNF-01 (Performance):** Latência de resposta da interface e API inferior a 2 segundos.
    * **Contexto:** Otimização de renderização via Chart.js para garantir fluidez na UI.
* **RNF-02 (Integridade de Dados):** Validação estrita de tipos e intervalos no Client-side e Server-side.
    * **Contexto:** Sanitização de inputs para valores monetários e restrições de calendário.
* **RNF-03 (Usabilidade e Design):** Interface adaptável baseada em Utility-First CSS (Tailwind).
    * **Contexto:** Garantia de responsividade e adoção de padrões de *Clean UI* para reduzir o esforço cognitivo.
* **RNF-04 (Eficiência de Estado):** Gerenciamento de estado local para redução de overhead.
    * **Contexto:** Uso de cache em memória (`dadosOriginais`) para permitir filtragem local, minimizando requisições redundantes ao backend.
* **RNF-05 (Persistência de Estado de Filtro):** Consistência da visualização pós-mutação de dados.
    * **Contexto:** O sistema deve manter o estado dos filtros ativos após operações de DELETE ou UPDATE.