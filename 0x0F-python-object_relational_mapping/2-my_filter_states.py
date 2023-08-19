#!/usr/bin/python3
'''
filter states by user input
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cr = db.cursor()
    cr.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
    states = cr.fetchall()

    for state in states:
        print(state)
