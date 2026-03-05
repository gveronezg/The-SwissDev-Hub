from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List, Optional
from models import Pedido
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Monta a pasta 'static' para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

pedidos_recebidos: List[Pedido] = []

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
    pedidos_recebidos.append(pedido)
    return pedido