from tables import users_table
from connect import engine
from sqlalchemy import select

statement = select(users_table).where(users_table.c.name == "Joe")

with engine.connect() as conn:
    result = conn.execute(statement)

    for row in result:
        print(f"<Username= {row.name} fullname={row.fullname}>")

        
'''with engine.connect() as conn:
    result = conn.execute(statement)

    for row in result:
        print(row)'''

"""with engine.connect() as conn:
    result = conn.execute(statement)

    for row in result:
        print(f"<Username= {row.name} fullname={row.fullname}>")"""

# To return only the name column in the table
#print(users_table.c.name)
#print(users_table.c.fullname)
#print(users_table.c.id)