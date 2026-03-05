const produto = document.getElementById('produto');
const diminuir = document.getElementById('diminuir');
const aumentar = document.getElementById('aumentar');
let quantidade = document.getElementById('quantidade');
const endereco = document.getElementById('endereco');
const contato = document.getElementById('contato');
const adicionar = document.getElementById('adicionar');
const itensAdicionados = document.getElementById('itens_adicionados');

diminuir.addEventListener('click', () => {
    if (quantidade.value > 0) {
        quantidade.value = parseInt(quantidade.value) - 1;
    }
});

aumentar.addEventListener('click', () => {
    quantidade.value = parseInt(quantidade.value) + 1;
});

const mapeamento = {
    "Batata de Costela": "qtd-costela",
    "Batata de Frango": "qtd-frango"
};

adicionar.addEventListener('click', () => {
    // 1. Qual produto foi escolhido?
    const produtoSelecionado = produto.value;

    // 2. Qual o ID da span desse produto?
    const idDaSpan = mapeamento[produtoSelecionado];

    // 3. Busca a span e muda o texto dela!
    document.getElementById(idDaSpan).innerText = quantidade.value;
});
