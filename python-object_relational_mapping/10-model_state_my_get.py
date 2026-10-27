#!/usr/bin/python3
"""model state my get"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).filter(
        State.name == sys.argv[4]).order_by(State.id).all()
    if not all_states:
        print("Not found")
    else:
        for state in all_states:
            print(f"{state.id}: {state.name}")

    session.close()
