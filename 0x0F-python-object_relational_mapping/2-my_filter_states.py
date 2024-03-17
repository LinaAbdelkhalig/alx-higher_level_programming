#!/usr/bin/python3
"""Module to lists all states starting with N"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    s = sys.argv[4]
    cmd = "SELECT * FROM states WHERE name='{}' ORDER BY states.id".format(s)
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
