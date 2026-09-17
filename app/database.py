import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

with engine.connect() as e:
    stmt = text("SELECT 1")
    response = e.execute(stmt)
    print(response.scalar())

class Base(DeclarativeBase):
    pass

