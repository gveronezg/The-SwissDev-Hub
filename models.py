# lib para fazer a validação dos dados json recebidos
from pydantic import BaseModel
from typing import List, Optional


class ItemPedido(BaseModel):
    produto: str
    quantidade: int


class Pedido(BaseModel):
    id: Optional[int] = None
    itens: List[ItemPedido]
    endereco: str
    contato: str
    total: float