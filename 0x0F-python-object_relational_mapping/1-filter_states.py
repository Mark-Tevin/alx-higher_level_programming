#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # Making connection to the database
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    # hence allowed to have same connection on multiple env
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
