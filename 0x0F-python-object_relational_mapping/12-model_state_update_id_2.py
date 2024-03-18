#!/usr/bin/python3
"""
this script changes the name of State
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

    # session classing
    Session = sessionmaker(bind=engine)

    # session objecting
    session = Session()

    # querying
    state = session.query(State).filter(State.id == 2).first()

    if state is not None:
        state.name = "New Mexico"

        # committing
        session.commit()

    # closing
    session.close()
