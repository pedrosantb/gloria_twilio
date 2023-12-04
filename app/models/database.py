
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:clg12345@clg-db.c6xallqtsbhv.sa-east-1.rds.amazonaws.com:5432/main"

engine = create_engine(
   SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
) #Take same thread arg when using production db

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



Base = declarative_base()