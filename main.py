from fastapi import FastAPI
from typing import List, Optional

app = FastAPI()

class Pedido:

    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade