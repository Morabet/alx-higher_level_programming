#!/usr/bin/python3

"""
changes the name of the State object where id=2 to New Mexico from a database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

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

    up_state = session.query(State).filter(State.id == 2).first()
    # Update the record
    if up_state:
        up_state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
