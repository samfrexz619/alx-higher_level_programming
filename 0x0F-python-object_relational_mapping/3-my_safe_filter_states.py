#!/usr/bin/python3
'''
list all values in the state table
'''
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name=%s;", (sys.argv[4],))
    [print(states) for states in cr.fetchall()]
