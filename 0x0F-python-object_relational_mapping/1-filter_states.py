#!/usr/bin/python3
"""
Lists all states with a name starting with N
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cr = db.cursor()
    cr.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cr.fetchall() if state[1][0] == "N"]
