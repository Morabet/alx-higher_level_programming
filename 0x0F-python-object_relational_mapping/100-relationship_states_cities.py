#!/usr/bin/python3

"""
creates the State California with the City San Francisco from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, name),
                           pool_pre_ping=True)

    # Create the tables
    Base.metadata.create_all(engine)
    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Start the Session
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)

    session.add(new_state, new_city)
    session.commit()

    # Close the session
    session.close()
