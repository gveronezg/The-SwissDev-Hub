from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from models import Pedido
from fastapi.staticfiles import StaticFiles
from database import iniciar_db, rodar_query, registrar_pedido, read_all_pedidos, update_pedido, delete_pedido
rodar_query(iniciar_db())

import os
from dotenv import load_dotenv
from httpx import post
load_dotenv()
URL_DISCORD = os.getenv("URL_DISCORD_WEBHOOK")

import json
texto_catalogo = os.getenv("CATALOGO", "{}")
PRECOS_OFICIAIS = json.loads(texto_catalogo)


def calcular_total(pedido: Pedido) -> float:
    total = 0.0
    if pedido.endereco.upper() != "RETIRADA":
        total += 10.0
    for item in pedido.itens:
        preco_unitario = PRECOS_OFICIAIS.get(item.produto, 0.0)
        total += preco_unitario * item.quantidade
    return total


app = FastAPI()

# Monta a pasta 'static' para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def iniciar_vendas():
    """ Tela raiz do sistema com os preços dos produtos disponiveis """
    return PRECOS_OFICIAIS


@app.get("/pedido")
def criar_pedido():
    # O 'with' é usado para garantir que o arquivo seja fechado logo após a leitura evitando erros de memória
    with open("static/criar_pedido.html", "r", encoding="utf-8") as html:
        conteudo = html.read()
        return HTMLResponse(content=conteudo)


@app.get("/pedidos")
def visualizar_pedidos():
    with open("static/manejar_pedidos.html", "r", encoding="utf-8") as html:
        conteudo = html.read()
        return HTMLResponse(content=conteudo)


@app.get("/manejar_pedidos")
def buscar_todos_pedidos():
    """
    Endpoint para buscar todos os pedidos registrados no banco de dados.
    """
    try:
        pedidos = read_all_pedidos()
        return {"pedidos": pedidos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/pedido")
def lancar_pedido(pedido: Pedido):
    # BLINDAGEM: Recalcula o total de forma segura no servidor
    pedido.total = calcular_total(pedido)

    # Crie o texto dos itens primeiro
    texto_itens = ""
    for item in pedido.itens:
        texto_itens += f"- {item.quantidade}x {item.produto}\n"

    try:
        mensagem_para_discord = f"""
**NOVO PEDIDO RECEBIDO!** 🍟
---------------------------
{texto_itens}
**Endereço:** {pedido.endereco}
**Contato:** {pedido.contato}
**TOTAL:** R$ {pedido.total:.2f}
"""
        # Envie na "caixa" que o Discord entende
        post(URL_DISCORD, json={"content": mensagem_para_discord})

        query, dados = registrar_pedido(pedido.model_dump())
        rodar_query(query, dados)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return pedido


@app.put("/manejar_pedidos")
def atualizar_pedido(pedido: Pedido):
    # BLINDAGEM: Recalcula o total de forma segura no servidor
    pedido.total = calcular_total(pedido)

    try:
        query, dados = update_pedido(pedido.model_dump())
        rodar_query(query, dados)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return pedido


@app.delete("/manejar_pedidos/{pedido_id}")
def deletar_pedido(pedido_id: int):
    try:
        query, dados = delete_pedido({"id": pedido_id}) 
        rodar_query(query, dados)
        return {"status": "sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    # O "main:app" diz: "Procure o objeto 'app' dentro do arquivo 'main.py'"
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)