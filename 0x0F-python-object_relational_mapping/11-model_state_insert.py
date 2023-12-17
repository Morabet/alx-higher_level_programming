#!/usr/bin/python3

"""adds the State object Louisiana to a database """

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

    # Insert a record into the database
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(f"{new_state.id}")
    # Close the session
    session.close()
