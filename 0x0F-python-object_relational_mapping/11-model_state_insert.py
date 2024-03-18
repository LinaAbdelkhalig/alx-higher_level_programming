#!/usr/bin/python3
"""
this script adds the State "louisiana"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    # engineing
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # classing
    Session = sessionmaker(bind=engine)

    # sessioning
    session = Session()

    # new state objecting
    new_state = State(name="Louisiana")

    # adding new state
    session.add(new_state)

    # committing the session to write the new State to the db
    session.commit()

    # printing the id
    print(new_state.id)

    # closing
    session.close()
