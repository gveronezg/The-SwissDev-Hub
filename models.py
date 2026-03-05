# lib para fazer a validação dos dados json recebidos
from pydantic import BaseModel

class Pedido(BaseModel):
    produto: str
    quantidade: int
    endereco: str
    contato: str