#!/usr/bin/python3
"""
Script that takes an arg and displays all values in states table
where name matches arguments
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # make a connection to the database

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])


    cur = conn.cursor()

    scrpt = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(scrpt)

    rows = cur.fetchall()
    for row in rows:
        print(row)
    # clean up process
    cur.close()
    conn.close()
