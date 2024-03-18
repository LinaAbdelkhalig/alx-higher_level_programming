#!/usr/bin/python3
"""
prints all the cities
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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
    for city, state in session.query(City, State) \
                       .join(State, City.state_id == State.id) \
                       .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # closing the session
    session.close()
