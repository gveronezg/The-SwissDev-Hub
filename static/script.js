const produto = document.getElementById('produto');
const diminuir = document.getElementById('diminuir');
const aumentar = document.getElementById('aumentar');
let quantidade = document.getElementById('quantidade');
const endereco = document.getElementById('endereco');
const contato = document.getElementById('contato');
const adicionar = document.getElementById('adicionar');
const itensAdicionados = document.getElementById('itens_adicionados');
const btnEnviar = document.getElementById('btnEnviar');

const mapeamento = {
    "Batata de Costela": "qtd-costela",
    "Batata de Frango": "qtd-frango"
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
    const idDaSpan = mapeamento[produtoSelecionado];

    // 3. Busca a span e muda o texto dela!
    document.getElementById(idDaSpan).innerText = quantidade.value;
});

btnEnviar.onclick = async () => {
    // 1. Monta o pacote (Objeto) em forma de dicionário
    const pedidoFinal = {
        produto: produto.value,
        quantidade: quantidade.value,
        endereco: endereco.value,
        contato: contato.value
    };
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
