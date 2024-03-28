#!/usr/bin/python3
"""
lists cities of state given as an argument from hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         password=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    SQL = "SELECT cities.name, states.name\
           FROM cities\
           INNER JOIN states\
           ON cities.state_id = states.id\
           ORDER BY cities.id ASC"
    curs.execute(SQL)
    cities = curs.fetchall()
    if cities is not None:
        print(", "
              .join(value[0] for value in cities if value[1] == sys.argv[4]))
    curs.close()
    db.close()
