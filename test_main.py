import pytest
from fastapi.testclient import TestClient
from main import app, calcular_total, verificar_credenciais
from models import Pedido, ItemPedido

# Removemos o override global para não afetar todos os testes
cliente = TestClient(app)

# Testes Unitários ##############################################

def test_calculo_total_com_entrega():
    """ 
    Garante que pedidos com endereço normal recebam a taxa de 10.00.
    Digamos que batata de costela = 40.0. Teremos 2 e 1 taxa.
    Total esperado = (40.0 * 2) + 10 = 90.0
    """
    # 1. PREPARAÇÃO (Arrange)
    item = ItemPedido(produto="Batata de Costela", quantidade=2)
    pedido = Pedido(
        itens=[item],
        endereco="Rua Teste, 123",
        contato="1199999999",
        total=0.0
    )
    
    # 2. AÇÃO (Act)
    total_calculado = calcular_total(pedido)
    
    # 3. VERIFICAÇÃO (Assert)
    # Aqui o script quebra se a matemática da sua função backend falhar!
    assert total_calculado == 90.0

def test_calculo_total_com_retirada():
    """
    Garante que pedidos marcados como RETIRADA não recebam taxa de entrega.
    """
    item = ItemPedido(produto="Batata de Frango", quantidade=1)
    pedido = Pedido(
        itens=[item],
        endereco="RETIRADA",
        contato="1199999999",
        total=0.0
    )
    
    total_calculado = calcular_total(pedido)
    
    # Batata de Frango no seu .env.example custa 35.0. Total = 35.0
    assert total_calculado == 35.0

# Testes de Integração ##########################################

def test_acesso_bloqueado_sem_senha_painel_adm():
    """ 
    Garante que entrar em /manejar_pedidos sem Basic Auth devolve 401 Unauthorized.
    """
    nova_requisicao = cliente.get("/manejar_pedidos")
    assert nova_requisicao.status_code == 401

def test_defesa_paginacao_contra_dos_limite_acima_de_cem():
    """ 
    Prevenção DoS!
    Se um atacante pedir limite=99999, o FastAPI deve responder 422 ao invés de
    ir no SQLite3 puxar todos os dados e arrebentar a memória.
    """
    # Aqui usamos o mock de Sobrescrita de Dependências para pular o Auth e testar apenas a funcionalidade
    """
    O problema é que lá no seu main.py original, a função verificar_credenciais() retorna uma string com o nome do usuário validado. Se a gente subistituir ela por nada, a rota ia quebrar por falta do nome. Então, a nossa "mini-função" lambda finge que fez todo o trabalho duro de validar a senha e simplesmente vomita uma string qualquer ("admin_falso") dizendo para a rota: "Pode passar, a senha tava certa, tá aqui o nome dele".
    """
    app.dependency_overrides[verificar_credenciais] = lambda: "admin_falso"
    nova_requisicao_maliciosa = cliente.get("/manejar_pedidos?limite=99999&offset=0")
    # Limpa o mock no fim para não poluir
    app.dependency_overrides.clear()
    
    # Tem que bater na parede do Pydantic Query()
    assert nova_requisicao_maliciosa.status_code == 422
    
def test_defesa_paginacao_contra_numeros_negativos():
    """ 
    Se o front end passar limit=-1 (um bug visual ou requisição forjada)
    """
    # Injetamos o mock APENAS neste teste
    app.dependency_overrides[verificar_credenciais] = lambda: "admin_falso"
    nova_requisicao = cliente.get("/manejar_pedidos?limite=-1&offset=0")
    app.dependency_overrides.clear()
    
    # Tem que ser rejeitado na hora, limite tem quer ser 'ge=1'
    assert nova_requisicao.status_code == 422