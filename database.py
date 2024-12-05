from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

USER = "sql12750063"
PASSWORD = "5L3gGkDjzR"
HOST = "sql12.freesqldatabase.com"
PORT = "3306"
NAME = "sql12750063"

URL_DATABASE = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

engine = create_engine( URL_DATABASE )
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

