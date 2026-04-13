const API_URL = 'http://127.0.0.1:8000'; 
let chartEvolucao = null;
let chartCategorias = null;
let dadosOriginais = [];

// 1. Alternar Seções
function showSection(name) {
    document.querySelectorAll('section').forEach(s => s.classList.add('hidden'));
    document.querySelectorAll('nav button').forEach(b => b.classList.remove('active-tab'));
    const section = document.getElementById(`sec-${name}`);
    if (section) section.classList.remove('hidden');
    const btn = document.getElementById(`btn-${name}`);
    if (btn) btn.classList.add('active-tab');
    
    carregarDados();
}

// 2. Controle visual dos botões de Tipo
function setTipo(t) {
    document.getElementById('tipo').value = t;
    const btnE = document.getElementById('btn-tipo-entrada');
    const btnS = document.getElementById('btn-tipo-saida');
    
    if(t === 'entrada') {
        btnE.className = "p-4 border-2 rounded-2xl font-bold transition border-green-600 text-green-600 bg-green-50";
        btnS.className = "p-4 border-2 rounded-2xl font-bold transition border-slate-200 text-slate-400";
    } else {
        btnS.className = "p-4 border-2 rounded-2xl font-bold transition border-red-600 text-red-600 bg-red-50";
        btnE.className = "p-4 border-2 rounded-2xl font-bold transition border-slate-200 text-slate-400";
    }
}

// 3. Busca Principal com Persistência de Filtro
async function carregarDados() {
    try {
        const res = await fetch(`${API_URL}/despesas`);
        if (!res.ok) throw new Error('Falha ao buscar dados');
        dadosOriginais = await res.json();
        
        const inicio = document.getElementById('filtro-inicio').value;
        const fim = document.getElementById('filtro-fim').value;

        if (inicio && fim) {
            aplicarFiltro(); 
        } else {
            renderLista(dadosOriginais);
            renderDashboard(dadosOriginais);
        }
    } catch (error) {
        console.error("Erro na API:", error);
    }
}

// 4. Renderizar Tabela de Transações
function renderLista(itens) {
    const corpo = document.getElementById('tabela-corpo');
    if (!corpo) return;
    
    corpo.innerHTML = '';
    itens.forEach(item => {
        const isEntrada = item.tipo === 'entrada';
        corpo.innerHTML += `
            <tr class="border-b hover:bg-slate-50 transition">
                <td class="p-5 text-slate-500 text-sm">${item.data}</td>
                <td class="p-5 font-bold text-slate-800">${item.descricao}</td>
                <td class="p-5"><span class="bg-slate-100 px-3 py-1 rounded-full text-xs font-bold text-slate-600">${item.categoria}</span></td>
                <td class="p-5 text-right font-bold ${isEntrada ? 'text-green-600' : 'text-red-600'}">
                    ${isEntrada ? '+' : '-'} R$ ${parseFloat(item.valor).toFixed(2)}
                </td>
                <td class="p-5 text-center">
                    <button onclick='deletar(${item.id})' class="text-slate-300 hover:text-red-500 transition">
                        <i class="fas fa-trash"></i>
                    </button>
                </td>
            </tr>
        `;
    });
}

function renderDashboard(itens) {
    const inicio = document.getElementById('filtro-inicio').value;
    const fim = document.getElementById('filtro-fim').value;
    const temFiltro = inicio && fim;

    const hoje = new Date();
    
    // 1. Gráfico fixo nos últimos 7 dias (Saídas)
    const seteDiasAtras = new Date();
    seteDiasAtras.setDate(hoje.getDate() - 7);
    
    const itensUltimos7Dias = dadosOriginais.filter(item => {
        const d = new Date(item.data + "T00:00:00");
        return d >= seteDiasAtras && d <= hoje && item.tipo === 'saida';
    });

    // 2. Cálculo dos cards (Entradas, Saídas, Saldo)
    let totalE = 0, totalS = 0, saldoGeral = 0;
    
    // Para o Saldo Geral, usamos SEMPRE tudo o que existe no banco
    dadosOriginais.forEach(item => {
        const v = parseFloat(item.valor);
        if (item.tipo === 'entrada') saldoGeral += v;
        else saldoGeral -= v;
    });

    // Para Entradas e Saídas, usamos os 'itens' (que podem estar filtrados ou não)
    itens.forEach(item => {
        const v = parseFloat(item.valor);
        if (item.tipo === 'entrada') totalE += v;
        else totalS += v;
    });

    const elementoQtd = document.getElementById('dash-qtd-transacoes');
    if (elementoQtd) {
        // itens.length pega a quantidade de itens na lista atual
        elementoQtd.innerText = `${itens.length} transações`;
    }

    document.getElementById('dash-saldo').innerText = `R$ ${saldoGeral.toFixed(2)}`;
    document.getElementById('dash-entradas').innerText = `R$ ${totalE.toFixed(2)}`;
    document.getElementById('dash-saidas').innerText = `R$ ${totalS.toFixed(2)}`;

    // 3. Lógica da Porcentagem
    const varSaida = document.getElementById('dash-variacao-saida');
    if (varSaida) {
        if (temFiltro) {
            const dataF = new Date(inicio + "T00:00:00");
            const mesAnterior = dataF.getMonth() - 1;
            const anoAnterior = mesAnterior < 0 ? dataF.getFullYear() - 1 : dataF.getFullYear();
            const mesBusca = mesAnterior < 0 ? 11 : mesAnterior;

            let gastosMesAnterior = 0;
            dadosOriginais.forEach(item => {
                const d = new Date(item.data + "T00:00:00");
                if (item.tipo === 'saida' && d.getMonth() === mesBusca && d.getFullYear() === anoAnterior) {
                    gastosMesAnterior += parseFloat(item.valor);
                }
            });

            if (gastosMesAnterior > 0) {
                const perc = ((totalS - gastosMesAnterior) / gastosMesAnterior) * 100;
                const cor = perc > 0 ? 'text-red-500' : 'text-green-500';
                varSaida.innerHTML = `<span class="${cor} font-bold">${perc > 0 ? '+' : ''}${perc.toFixed(1)}%</span> vs. mês anterior`;
            } else {
                varSaida.innerHTML = `<span class="text-slate-400">Sem dados do mês anterior</span>`;
            }
        } else {
            varSaida.innerHTML = `<span class="text-slate-400 font-bold">Total Acumulado</span>`;
        }
    }

    // 4. Mandar rodar o gráfico com os 7 dias
    updateChartEvolucao(itens);

    // Gráfico de Categorias
    const resumoCategorias = {};
    itens.filter(i => i.tipo === 'saida').forEach(i => {
        resumoCategorias[i.categoria] = (resumoCategorias[i.categoria] || 0) + parseFloat(i.valor);
    });
    updateChartCategorias(Object.entries(resumoCategorias).sort((a, b) => b[1] - a[1]).slice(0, 5));
}

// 6. Gráfico de Evolução (Mostrando os dados enviados, ex: últimos 7 dias)
function updateChartEvolucao(itensGrafico) {
    const canvas = document.getElementById('chartEvolucao');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (chartEvolucao) chartEvolucao.destroy();

    // Organizar por data para o gráfico não ficar "vai e volta"
    const itensOrdenados = [...itensGrafico].sort((a, b) => new Date(a.data) - new Date(b.data));

    // Pegamos as datas e os valores
    const labels = itensOrdenados.map(item => {
        const d = new Date(item.data);
        return d.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit' });
    });
    const valores = itensOrdenados.map(item => parseFloat(item.valor));

    chartEvolucao = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Gastos (7 dias)',
                data: valores,
                borderColor: '#ef4444', // Vermelho para gastos
                backgroundColor: 'rgba(239, 68, 68, 0.1)',
                fill: true,
                tension: 0.3
            }]
        },
        options: { 
            responsive: true, 
            maintainAspectRatio: false, 
            plugins: { legend: { display: false } },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// 7. Gráfico de Categorias
function updateChartCategorias(dadosCategorias) {
    const canvas = document.getElementById('chartCategorias');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (chartCategorias) chartCategorias.destroy();
    
    chartCategorias = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: dadosCategorias.map(c => c[0]),
            datasets: [{
                data: dadosCategorias.map(c => c[1]),
                backgroundColor: '#3b82f6',
                borderRadius: 8
            }]
        },
        options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }
    });
}

// 8. Enviar Despesa com Validação
const formDespesa = document.getElementById('form-despesa');

if (formDespesa) {
    formDespesa.addEventListener('submit', async function(e) {
        e.preventDefault(); // Impede a página de recarregar
        console.log("1. Formulário interceptado com sucesso!");
        
        const dataInput = document.getElementById('data').value;
        if (!dataInput) {
            alert("Por favor, preencha a data.");
            return;
        }
        
        const anoSelecionado = new Date(dataInput).getUTCFullYear(); 
        if (anoSelecionado > 2100 || anoSelecionado < 1900) {
            alert("Por favor, insira um ano entre 1900 e 2100.");
            return;
        }

        const desc = document.getElementById('descricao').value;
        const valor = parseFloat(document.getElementById('valor').value);
        const tipo = document.getElementById('tipo').value;
        const cat = document.getElementById('categoria').value;
        
        if (!desc || isNaN(valor) || valor <= 0 || !cat) {
            alert("Preencha todos os campos corretamente.");
            return;
        }

        const payload = { descricao: desc, valor, data: dataInput, categoria: cat, tipo };
        console.log("2. Dados prontos:", payload);

        try {
            const res = await fetch(`${API_URL}/despesas`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });

            if(res.ok) {
                console.log("3. Salvo no banco com sucesso!");
                formDespesa.reset(); 
                setTipo('saida');
                await carregarDados(); 
                showSection('dashboard');
            } else {
                const erro = await res.json();
                console.error("Erro do backend:", erro);
                alert("Erro no servidor: " + JSON.stringify(erro.detail));
            }
        } catch (err) {
            console.error("Falha na conexão:", err);
            alert("Erro ao conectar com o servidor.");
        }
    });
}

// 9. Deletar Transação
async function deletar(id) {
    if(confirm("Deseja excluir definitivamente esta transação?")) {
        await fetch(`${API_URL}/despesas/${id}`, { method: 'DELETE' });
        carregarDados();
    }
}

// 10. Funções de Filtro
function aplicarFiltro() {
    const inicio = document.getElementById('filtro-inicio').value;
    const fim = document.getElementById('filtro-fim').value;
    
    if (!inicio || !fim) return;

    const filtrados = dadosOriginais.filter(item => {
        return item.data >= inicio && item.data <= fim;
    });

    renderLista(filtrados);
    renderDashboard(filtrados);
}

function limparFiltro() {
    document.getElementById('filtro-inicio').value = '';
    document.getElementById('filtro-fim').value = '';
    renderLista(dadosOriginais);
    renderDashboard(dadosOriginais);
}

// Inicialização
carregarDados();