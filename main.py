# dicionário
novo_recurso = {
    "titulo": "calculadora",
    "link": "...",
}

descricao_final = novo_recurso.get("descricao","Sem descrição informada.")


def do_get(dicionario, chaves, senao):
    for chave in chaves:
        print(dicionario.get(chave, senao))


chaves = ["titulo","link","descricao"]
do_get(novo_recurso,chaves,"Chave não encontrada!")

print(descricao_final)