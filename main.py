from typing import List

# criando uma variável tipada como Lista de Dicionários
banco_dados: List[dict] = [
]
CATEGORIAS_PERMITIDAS: tuple = ("FrontEnd", "BackEnd", "DevOps")
categoria_nova = "Mobile"

if categoria_nova in CATEGORIAS_PERMITIDAS:
    pass
else:
    print(f'Categoria {categoria_nova} é inválida.')

# O -> None indica que a função faz uma ação, mas não devolve nenhum valor de volta
def adicionar_recurso(dados_recurso: dict) -> None:
    banco_dados.append(dados_recurso)


# dicionário
novo_recurso = {
    "titulo": "calculadora",
    "link": "...",
}
adicionar_recurso(novo_recurso)
print(banco_dados)

descricao_final = novo_recurso.get("descricao","Sem descrição informada.")
print(descricao_final)


def do_get(dicionario, chaves, senao):
    for chave in chaves:
        print(dicionario.get(chave, senao))


chaves = ["titulo", "link", "descricao"]
do_get(novo_recurso,chaves,"Chave não encontrada!")