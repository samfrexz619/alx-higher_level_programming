#!/usr/bin/python3
'''
print the state obj
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    is_present = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print(f'{state.id}')
            is_present = True
            break
    if is_present is False:
        print('Not found')
