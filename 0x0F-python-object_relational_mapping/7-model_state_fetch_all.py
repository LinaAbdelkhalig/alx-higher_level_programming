#!/usr/bin/python3
"""
List all the state objects from the db
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # setting up db engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # creating a session class
    Session = sessionmaker(bind=engine)

    # creating a session
    session = Session()

    # querying
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    # closing the session
    session.close()
