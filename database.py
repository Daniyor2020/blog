from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


 

# encoded_username = quote_plus(MYSQL_USERNAME)
encoded_password = quote_plus("Dani@2022")
 

USER = "root"
PASSWORD = encoded_password
HOST = "localhost"
PORT = "3306"
NAME = "smart_kids"
URL_DATABASE = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

engine = create_engine( URL_DATABASE )
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

