#!/usr/bin/python3
"""
lists states from hbtn_0e_0_usa that match a given argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    SQL = "SELECT id, name\
           FROM states\
           WHERE BINARY name = '{}'\
           ORDER BY id ASC".format(sys.argv[4])
    curs.execute(SQL)
    states = curs.fetchall()
    if states is not None:
        [print(state) for state in states]
    curs.close()
    db.close()
