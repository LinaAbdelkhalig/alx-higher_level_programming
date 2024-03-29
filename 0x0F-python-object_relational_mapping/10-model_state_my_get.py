#!/usr/bin/python3
"""
this script prints states that haave an a in their name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    # setting up the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # creating a session class
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # querying
    state = session.query(State) \
        .filter(State.name == sys.argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    # close the session
    session.close()
