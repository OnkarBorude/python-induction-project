"""
Docstring for Day8.database_op
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus



load_dotenv(".env")

DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_NAME=os.getenv("DB_NAME")
DB_PORT=os.getenv("DB_PORT")

encoded_password = quote_plus(DB_PASSWORD)

DATABASE_URL= (
    f"mysql+pymysql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine= create_engine(
    DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False , autoflush=False, bind=engine)

Base=declarative_base()

def get_db():
    """
    Docstring for get_db
    """
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


print("Base is:", Base)

# from dotenv import load_dotenv
# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# ENV_PATH = os.path.join(BASE_DIR, ".env")

# print("Loading ENV file from:", ENV_PATH)
# load_dotenv(ENV_PATH)

# print("DEBUG -> DB_HOST:", os.getenv("DB_HOST"))
# print("DEBUG -> DB_PORT:", os.getenv("DB_PORT"))
# print("DEBUG -> DB_USER:", os.getenv("DB_USER"))
# print("DEBUG -> DB_PASSWORD:", os.getenv("DB_PASSWORD"))
# print("DEBUG -> DB_NAME:", os.getenv("DB_NAME"))