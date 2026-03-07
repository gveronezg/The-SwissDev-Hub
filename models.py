# lib para fazer a validação dos dados json recebidos
from pydantic import BaseModel
from typing import List


class ItemPedido(BaseModel):
    produto: str
    quantidade: int


class Pedido(BaseModel):
    itens: List[ItemPedido]
    endereco: str
    contato: str
    total: float