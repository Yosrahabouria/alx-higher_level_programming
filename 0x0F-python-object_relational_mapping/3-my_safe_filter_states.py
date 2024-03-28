#!/usr/bin/python3
"""
lists states from the database hbtn_0e_0_usa that match a given argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    SQL = "SELECT id, name\
           FROM states\
           WHERE name = %(username)s\
           ORDER BY id ASC"
    curs.execute(SQL, {'username': sys.argv[4]})
    states = curs.fetchall()
    if states is not None:
        for row in states:
            print("({}, '{}')".format(row[0], row[1]))
        curs.close()
        db.close()
