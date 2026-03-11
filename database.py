import sqlite3
import json


def rodar_query(query, parms=(), retorno=False):
    with sqlite3.connect('pedidos.db') as con:
        if retorno:
            con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(query, parms)

        if retorno:
            return cur.fetchall()

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


def read_all_pedidos():
    """
    Busca todos os pedidos registrados no banco de dados.
    """
    query = "SELECT * FROM pedidos"
    rows = rodar_query(query, retorno=True)
    # Convertendo os resultados usando os nomes das colunas
    pedidos = []
    for row in rows:
        pedidos.append({
            'id': row['id'],
            'itens': json.loads(row['itens']),  # Convertendo JSON de volta para dicionário
            'endereco': row['endereco'],
            'contato': row['contato'],
            'total': row['total']
        })
    return pedidos


def update_pedido(pedido_dict):
    """
    Atualizando o pedido no BD
    """
    itens_json = json.dumps(pedido_dict['itens'])
    query = """
        UPDATE pedidos SET itens = ?, endereco = ?, contato = ?, total = ? WHERE id = ?
    """
    return query, (itens_json, pedido_dict['endereco'], pedido_dict['contato'], pedido_dict['total'], pedido_dict['id'])


def delete_pedido(pedido_dict):
    """
    Deletando o pedido no BD
    """
    query = """
        DELETE FROM pedidos WHERE id = ?
    """
    return query, (pedido_dict['id'],)


# Se você não usa o if __name__ == "__main__":, toda vez que o seu main.py fizer o import, ele vai criar a tabela no banco de novo (o que pode causar erros ou lentidão). Se você usa, o código só vai rodar se você executar o arquivo database.py diretamente no terminal.
if __name__ == "__main__":
    db_init = iniciar_db()
    rodar_query(db_init)