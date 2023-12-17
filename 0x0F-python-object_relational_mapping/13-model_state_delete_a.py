#!/usr/bin/python3

"""
a script that deletes all 'State objects' with a 'name'
containing the letter 'a' from the database hbtn_0e_6_usa
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

    del_state = session.query(State).filter(State.name.like("%a%")).all()

    #  Delete the record if it exists
    if del_state:
        for dell in del_state:
            session.delete(dell)

        session.commit()

    # Close the session
    session.close()
