const produto = document.getElementById('produto');
const diminuir = document.getElementById('diminuir');
const aumentar = document.getElementById('aumentar');
let quantidade = document.getElementById('quantidade');
const endereco = document.getElementById('endereco');
const contato = document.getElementById('contato');
const adicionar = document.getElementById('adicionar');
const itensAdicionados = document.getElementById('itens_adicionados');
const btnEnviar = document.getElementById('btnEnviar');
const retirar = document.getElementById('entrega_off');

const mapeamento = {
    "Batata de Costela": { qtdId: "qtd-costela", totalId: "total-costela", preco: 40.0 },
    "Batata de Frango": { qtdId: "qtd-frango", totalId: "total-frango", preco: 35.0 }
};

diminuir.addEventListener('click', () => {
    if (quantidade.value > 0) {
        quantidade.value = parseInt(quantidade.value) - 1;

    }
});

aumentar.addEventListener('click', () => {
    // parseInt serve para converter o valor do input para número
    quantidade.value = parseInt(quantidade.value) + 1;
});

adicionar.addEventListener('click', () => {
    // 1. Qual produto foi escolhido?
    const produtoSelecionado = produto.value;

    // 2. Qual o ID da span desse produto?
    const idDaSpan = mapeamento[produtoSelecionado].qtdId;

    // 3. Busca a span e muda o texto dela!
    document.getElementById(idDaSpan).innerText = quantidade.value;

    // 4. Atualiza o total
    document.getElementById(mapeamento[produtoSelecionado].totalId).innerHTML = mapeamento[produtoSelecionado].preco * quantidade.value;
});

retirar.addEventListener('click', () => {
    if (retirar.checked) {
        document.getElementById('receber').style.display = 'none'
        endereco.value = "RETIRADA"
    } else { document.getElementById('receber').style.display = 'block'; endereco.value = "" }
})

btnEnviar.onclick = async () => {

    let totalDoPedido = 0
    if (!retirar.checked) { totalDoPedido += 10; }
    const itensDoPedido = []
    // varrendo cada produto cadastrado
    for (const nomeProduto in mapeamento) {
        // obtem a quantidade definida no pedido
        let qtd = parseInt(document.getElementById(mapeamento[nomeProduto].qtdId).innerText);
        if (qtd > 0) {
            // somar o valor total deste item ao total do pedido
            totalDoPedido += (mapeamento[nomeProduto].preco * qtd)
            // adiciona o item ao pedido
            itensDoPedido.push({ produto: nomeProduto, quantidade: parseInt(qtd) })
        }
    }
    if (itensDoPedido.length === 0) { alert("Sua sacola está vazia!"); return; }

    resumoItens = ""
    for (const item of itensDoPedido) {
        resumoItens += `${item.quantidade}x ${item.produto}\n`
    }

    const mensagem = `CONFIRMAR PEDIDO:\n
Itens:
${resumoItens}
Endereço: ${endereco.value}
Contato: ${contato.value}
Total: R$ ${totalDoPedido.toFixed(2)}`

    if (!confirm(mensagem)) { return; }

    // 1. Monta o pacote (Objeto) em forma de dicionário
    const pedidoFinal = {
        itens: itensDoPedido,
        endereco: endereco.value,
        contato: contato.value,
        total: totalDoPedido
    }
    console.log(pedidoFinal);

    // 2. Envia para o Back-end Python
    const resposta = await fetch('/pedido', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Avisa que está enviando JSON
        },
        body: JSON.stringify(pedidoFinal) // Transforma o objeto em texto
    });

    // 3. Recebe a resposta
    const resultado = await resposta.json();
    alert("Pedido enviado com sucesso para: " + resultado.endereco);
};
