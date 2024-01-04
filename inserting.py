from sqlalchemy import insert
from tables import users_table
from connect import engine

statement = insert(users_table)

with engine.connect() as conn:
    conn.execute(statement, [
        {'name': "Joe", "fullname": "Joe Biden"},
        {'name': "Desmond", "fullname": "Desmond Abiola"},
        {'name': "Ehis", "fullname": "Ehis Evans"}
    ])

    conn.commit()