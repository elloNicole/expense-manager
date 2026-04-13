## Processo: Registro de Transação (Entradas e Saídas)
Ator: Usuário

1. Acesso: Usuário acessa o formulário de cadastro na interface.

2. Entrada de Dados: Preenche descrição, valor, data, categoria e seleciona o tipo (Entrada/Saída).

3. Validação de Interface: O sistema valida se todos os campos estão preenchidos e se a data é consistente.

4. Sincronização API: O sistema envia os dados para o backend via POST e armazena no banco de dados.

5. Atualização Dinâmica: O sistema recarrega os dados globais e redireciona o usuário para o Dashboard atualizado.

6. Resultado:
    Registro estruturado e padronizado de movimentações financeiras.

    Redução drástica de erros de digitação e esquecimentos.

## Processo: Análise e Filtragem de Dados (Dashboard)
Ator: Usuário e Sistema

1. Interação: Usuário define um período inicial e final no filtro de calendário.

2. Processamento de Dados: O sistema filtra o array de transações em tempo real (sem recarregar a página).

3. Cálculo de Inteligência:
    O sistema identifica se há um mês fechado selecionado.

    Busca no histórico o valor do mês anterior para gerar o comparativo percentual (%).

4. Renderização Visual:
    Os cards de totalizadores são atualizados.

    O gráfico de evolução redesenha a linha de gastos baseada estritamente no período escolhido.

    O gráfico de categorias ajusta as proporções de gastos.

5. Resultado:
    Visibilidade clara sobre o comportamento financeiro em janelas de tempo específicas.

    Capacidade de auditoria rápida de meses anteriores.

## Comparativo de Maturidade do Projeto

Antes (Cenário Inicial)
1. Controle manual: Dependência de planilhas complexas ou anotações físicas.

2. Baixa visibilidade: Difícil identificar tendências ou comparar meses sem cálculos manuais exaustivos.

3. Dados isolados: Informações descentralizadas e propensas a perdas.

Depois (Com o Novo Sistema)
1. Sistema Centralizado: Uma única fonte da verdade para todas as finanças.

2. Gráficos de Decisão: Visualização imediata de onde o dinheiro está sendo gasto (Categorias) e como ele flui (Evolução).

4. Inteligência Comparativa: A variação percentual automática permite entender o crescimento ou redução de custos de forma rápida.

5. Dados Organizados: Interface limpa que prioriza a leitura rápida dos indicadores de saúde financeira.