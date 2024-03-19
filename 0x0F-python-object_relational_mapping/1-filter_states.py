#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    SQL = "SELECT id, name FROM states ORDER BY id ASC"
    curs.execute(SQL)
    states = curs.fetchall()
    if states is not None:
        [print(state) for state in states if state[1][0] == "N"]
    curs.close()
    db.close()
