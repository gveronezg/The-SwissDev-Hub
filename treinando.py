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
do_get(novo_recurso, chaves, "Chave não encontrada!")


tags_exemplo = ["python", "api", "python", "fastapi"]
# set é um construtor que retorna cada elemento encontrado
tags_unicas = set(tags_exemplo)
print(tags_unicas)

top_tags = list(tags_unicas)[0:2]
print(top_tags)

usuarios_novos = ["gabriel", "ana", "pedro",]
usuarios_vip = [t.capitalize() for t in usuarios_novos]
print(usuarios_vip)

precos = [10.50, 4.00, 15.00, 8.00, 20.00]
precos_vip = [p for p in precos if p > 10]
print(precos_vip)


class Recurso:

    def __init__(self, titulo: str, link: str):
        self.titulo = titulo
        self.link = link

    def __str__(self) -> str:
        return f"Recurso: {self.titulo}\nLink: {self.link}"

class RecursoVideo(Recurso):

    def __init__(self, titulo: str, link: str, duracao: int):
        super().__init__(titulo, link)
        self.duracao = duracao

class RecursoArtigo(Recurso):

    def __init__(self, titulo: str, link: str, autor: str):
        super().__init__(titulo, link)
        self.autor = autor

meu_recurso = Recurso("FastAPI", "https://...")
print(meu_recurso)
meu_video = RecursoVideo('teyba', 'xuleiba', 120)
print(meu_video.titulo)
print(meu_video.duracao)

