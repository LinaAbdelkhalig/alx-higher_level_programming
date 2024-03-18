#!/usr/bin/python3
""" A model that contains the class definition of a state and instance
    Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base.

    Attributes:
        __tablename__ (str): the name of the mysql table
        id (sqlalchemy.Column): The state's id.
        name (sqlalchemy.Column): the state's name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
