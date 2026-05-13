from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#passo 1 - declarar a url do banco

POSTGRESS_DATABASE_URL = "postgresql://user:password@postgress/mydatabase"

#passo 2 - criar engine
engine = create_engine(POSTGRESS_DATABASE_URL)

#passo 3 - criar session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#passo 4 - criar base
Base = declarative_base() #ORM

#passo 5 - definição de rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
