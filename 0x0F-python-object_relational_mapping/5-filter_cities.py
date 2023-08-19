#!/usr/bin/python3
'''
lists all cities of that state, using the database hbtn_0e_4_usa
'''
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cr = db.cursor()
    cr.execute("SELECT * FROM cities JOIN states \
                ON cities.state_id = states.id ORDER BY cities.id")
    [print(", ".join([c[2] for c in cr.fetchall() if c[4] == sys.argv[4]]))]
