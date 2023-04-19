from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

def db_init():
    DB_HOST = 'postgresql.local'
    DB_USER = 'postgres'
    DB_PASS = 'postgres'

    url = URL.create(
        drivername="postgresql",
        username=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        database="todos",
        port=5432
    )
    engine = create_engine(url)

    return engine

def print_tables(engine):
    print('Table info')
    inspector = inspect(engine)
    print(inspector.get_table_names())

