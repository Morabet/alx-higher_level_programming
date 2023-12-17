#!/usr/bin/python3
"""
prints all City objects from a database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, name),
                           pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Start the Session
    session = Session()

    result = session.query(State.name, City.id, City.name).join(
            State, State.id == City.state_id).all()
    for row in result:
        print(f"{row[0]}: ({row[1]}) {row[2]}")

    # Close the session
    session.close()
