import sqlite3
import json


def rodar_query(query, parms=()):
    with sqlite3.connect('pedidos.db') as con:
        cur = con.cursor()
        cur.execute(query, parms)
        con.commit()


def iniciar_db():
    """
    Conecting to SQLiteDB and creating a table if it does not exist.
    """
    query = """
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            itens TEXT,
            endereco TEXT,
            contato TEXT,
            total REAL
        )
    """
    return query


def registrar_pedido(pedido_dict):
    """
    Registring the order on the BD
    """
    itens_json = json.dumps(pedido_dict['itens'])
    query = """
        INSERT INTO pedidos (itens, endereco, contato, total) VALUES (?, ?, ?, ?)
    """
    return query, (itens_json, pedido_dict['endereco'], pedido_dict['contato'], pedido_dict['total'])

# Se você não usa o if __name__ == "__main__":, toda vez que o seu main.py fizer o import, ele vai criar a tabela no banco de novo (o que pode causar erros ou lentidão). Se você usa, o código só vai rodar se você executar o arquivo database.py diretamente no terminal.
if __name__ == "__main__":
    db_init = iniciar_db()
    rodar_query(db_init)