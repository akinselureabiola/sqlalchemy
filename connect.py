import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sample.db",echo=True)

with engine.connect() as conn:
    result = conn.execute(text('SELECT "Hello, how are you ?"'))

    print(result.all())
