from sqlalchemy import create_engine
from sqlalchemy.ext.declaration import declaration_base
from sqlalchemy.orm import sessionmaker


SQLALCHAMY_DATABASE_URL = 'sqlite:///:/blog.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL,{"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

base = declaration_base()
