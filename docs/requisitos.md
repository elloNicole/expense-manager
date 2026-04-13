## Requisitos Funcionais
REQ-01: O sistema deve permitir o cadastro de transações

    Descrição: O usuário deve ser capaz de registrar entradas e saídas informando descrição, valor, data, categoria e tipo.

    Validação: O sistema deve diferenciar visualmente entradas de saídas no momento do cadastro para evitar erros operacionais.

REQ-02: O sistema deve permitir a exclusão de transações

    Descrição: O sistema deve oferecer a opção de remover registros diretamente da tabela de transações.

    Validação: Deve haver uma confirmação de segurança (prompt) antes da exclusão definitiva no banco de dados.

REQ-03: O sistema deve exibir dashboard financeiro dinâmico

    Descrição: O sistema deve apresentar cards com Saldo Geral, Total de Entradas e Total de Saídas.

    Validação: Os cards de entradas e saídas devem reagir aos filtros de data aplicados pelo usuário.

REQ-04: O sistema deve gerar gráficos de evolução e categorias

    Descrição: O sistema deve renderizar um gráfico de linha para a evolução dos gastos e um gráfico de barras para a distribuição por categorias.

    Validação: O gráfico de evolução deve ser recalculado automaticamente para refletir o resumo do período filtrado.

REQ-05: O sistema deve calcular variação percentual mensal

    Descrição: Ao filtrar um mês específico, o sistema deve comparar o total de gastos com o mês imediatamente anterior.

    Validação: Caso não haja filtro aplicado, o sistema deve exibir o total acumulado sem gerar cálculos de variação incoerentes.

REQ-06: O sistema deve permitir filtragem por período

    Descrição: O usuário deve poder definir uma data inicial e final para visualizar transações específicas.

## Requisitos Não Funcionais
    RNF-01: O sistema deve possuir tempo de resposta inferior a 2 segundos.

    Contexto: A comunicação com a API (CRUD) e a atualização dos gráficos via Chart.js devem ser quase instantâneas para garantir fluidez.

RNF-02: O sistema deve garantir validação e integridade dos dados de entrada.

    Contexto: Datas devem estar dentro de um intervalo real (ex: 1900-2100), valores devem ser positivos e campos obrigatórios não podem ser nulos.

RNF-03: O sistema deve possuir interface simples, intuitiva e responsiva.

    Contexto: Utilização de Tailwind CSS para garantir que o dashboard seja legível em diferentes resoluções e mantenha um padrão visual limpo (Clean UI).

RNF-04: O sistema deve gerenciar estados de forma otimizada.

    Contexto: O uso da variável dadosOriginais permite que o sistema filtre informações localmente sem a necessidade de múltiplas requisições idênticas ao banco de dados, economizando banda e processamento.

RNF-05: O sistema deve garantir a persistência de filtros durante a navegação.

    Contexto: Ao excluir uma transação enquanto um filtro está ativo, a lista deve ser recarregada mantendo o filtro aplicado anteriormente.