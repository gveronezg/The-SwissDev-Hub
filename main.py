from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import Pedido
from fastapi.staticfiles import StaticFiles
from database import iniciar_db, rodar_query, registrar_pedido
rodar_query(iniciar_db())

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
        print(f"Erro ao processar pedido: {e}")

    return pedido

if __name__ == "__main__":
    import uvicorn
    # O "main:app" diz: "Procure o objeto 'app' dentro do arquivo 'main.py'"
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)