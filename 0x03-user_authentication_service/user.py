#!/usr/bin/env python3
"""User model for SQLAlchemy"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for the model
Base = declarative_base()

class User(Base):
    """User class representing a user in the database"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

# Set up the database engine to interact with the database
engine = create_engine('sqlite:///user.auth.db')

# Create all the tables in the database
Base.metadata.create_all(engine)

# Create a configured "Session" class and instantiate a session object
Session = sessionmaker(bind=engine)
session = Session()

