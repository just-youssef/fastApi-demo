from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from os import environ
from models import Base

# PostgreSQL DB_URI
DB_URI = environ['DB_URI']

# SQLAlchemy engine
engine = create_engine(DB_URI)

# Base class for ORM models
Base.metadata.create_all(engine, checkfirst=True)

# Create a sessionmaker to bind the engine with session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

