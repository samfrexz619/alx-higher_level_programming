#!/usr/bin/python3
'''
filter states by user input
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE BINARY name = f'{sys.argv[4]}'")
    [print(state) for state in cr.fetchall()]
