let pedidosSalvos = [];

// 1. Função que busca os dados da API no BD
async function carregarTabela() {

    // Roda a função da rota /manejar_pedidos que vai chamar a função do banco de dados e obter os dados
    const resposta = await fetch('/manejar_pedidos');
    // Absorvando apenas o corpo json da resposta
    const dados = await resposta.json();
    // Fragmentando o json para obter uma lista com cada pedido
    const listaDePedidos = dados.pedidos;
    // Salva uma cópia na memória do servidor
    pedidosSalvos = listaDePedidos;

    const corpoTabela = document.getElementById("corpo-tabela");
    // Limpando a tabela antes de carregar os dados
    corpoTabela.innerHTML = "";


    // 2. Percorrendo a lista de pedidos
    listaDePedidos.forEach(pedido => {

        // Vamos melhorar a visualização da string json de itens
        const resumoItens = pedido.itens
            .map(item => `${item.quantidade}x${item.produto}`)
            .join(" & ");

        // Criando uma linha para cada pedido
        const linha = document.createElement("tr");

        // Criando as colunas com os dados
        linha.innerHTML = `
            <td>${pedido.id}</td>
            <td>${resumoItens}</td>
            <td>${pedido.endereco}</td>
            <td>${pedido.contato}</td>
            <td>R$ ${pedido.total.toFixed(2)}</td>
            <td>
                <button onclick="editarPedido(${pedido.id})">✏️</button>
                <button onclick="excluirPedido(${pedido.id})">🗑️</button>
            </td>
        `;

        // Adicionando a linha na tabela
        corpoTabela.appendChild(linha);
    });
}

// 3. Roda a função assim que carregar
carregarTabela();

// 4. Função para excluir
async function excluirPedido(id) {
    // Pergunta pro usuário se ele tem certeza
    if (!confirm("Tem certeza que deseja excluir o pedido " + id + "?")) {
        return; // Para a função se ele cancelar
    }

    // Chama a rota /excluir_pedido passando o ID
    await fetch(`/manejar_pedidos/${id}`, {
        method: "DELETE" // Método HTTP DELETE
    });

    // Recarrega a tabela para mostrar a mudança
    carregarTabela();
}

// 5. Função para editar
async function editarPedido(id) {
    // Procura na memória o objeto com o ID selecionado
    const pedido = pedidosSalvos.find(p => p.id === id);

    if (pedido) {
        // Preenche o formulário de edição com os dados reais
        document.getElementById('id').value = pedido.id;
        for (let i = 0; i < pedido.itens.length; i++) {
            if (pedido.itens[i].quantidade > 1) {
                document.getElementById('item').value = pedido.itens[i].produto;
                document.getElementById('qtd').value = pedido.itens[i].quantidade;
            }
        }
        document.getElementById('endereco').value = pedido.endereco;
        document.getElementById('total').value = pedido.total;
    }
}