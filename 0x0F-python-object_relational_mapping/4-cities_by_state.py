#!/usr/bin/python3
"""
Script that lists all cities from hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         password=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    SQL = "SELECT cities.id, cities.name, states.name\
           FROM cities\
           INNER JOIN states\
           ON cities.state_id = states.id\
           ORDER BY cities.id ASC"
    curs.execute(SQL)
    cities = curs.fetchall()
    if cities is not None:
        for item in cities:
            print("({}, '{}', '{}')".format(item[0], item[1], item[2]))
        curs.close()
        db.close()
