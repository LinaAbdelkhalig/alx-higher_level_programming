#!/usr/bin/python3
""" A model that contains the class definition of a city and instance
    Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    City class that inherits from Base.

    Attributes:
        __tablename__ (str): the name of the mysql table
        id (sqlalchemy.Column): The city's id.
        name (sqlalchemy.Column): the city's name
        state_id (sqlalchemy.Column): foreign key
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
