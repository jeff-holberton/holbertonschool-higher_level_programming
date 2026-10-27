#!/usr/bin/python3
"""model city fetch by state"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(City, State).join(
        State, City.state_id == State.id).order_by(City.id).all()
    for city, state in all_states:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
