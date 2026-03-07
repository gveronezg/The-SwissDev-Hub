from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List, Optional
from models import Pedido
from fastapi.staticfiles import StaticFiles

import os
from dotenv import load_dotenv
from httpx import post

load_dotenv()
URL_DISCORD = os.getenv("URL_DISCORD_WEBHOOK")


app = FastAPI()

# Monta a pasta 'static' para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def raiz():
    return "Você esta na raiz da API."

@app.get("/pedido")
def criar_pedido():
    # O 'with' é usado para garantir que o arquivo seja fechado logo após a leitura evitando erros de memória
    with open("criar_pedido.html", "r", encoding="utf-8") as html:
        conteudo = html.read()
        return HTMLResponse(content=conteudo)

@app.post("/pedido")
def lancar_pedido(pedido: Pedido):
    # Crie o texto dos itens primeiro
    texto_itens = ""
    for item in pedido.itens:
        texto_itens += f"- {item.quantidade}x {item.produto}\n"

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

    return pedido
