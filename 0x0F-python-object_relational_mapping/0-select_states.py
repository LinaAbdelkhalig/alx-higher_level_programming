#!/usr/bin/python3
"""Module to lists all states from hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_states():
    """function that lists all the states sorted by state id"""

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
