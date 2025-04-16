# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os

# Replace with your actual PostgreSQL credentials
DATABASE_URL="postgresql://postgres:Next%40123@localhost:5432/Muktananda"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create tables if not exist
Base.metadata.create_all(engine)
