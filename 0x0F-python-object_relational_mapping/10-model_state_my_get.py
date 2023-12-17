#!/usr/bin/python3

"""prints the State object with the name passed as argument from a database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    name = argv[3]
    search = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, name),
                           pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Start the Session
    session = Session()

    result = session.query(State).filter(State.name == search).all()
    if result:
        for row in result:
            print(f"{row.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
