#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
# import sys
# import MySQLdb
import mysql.connector

if __name__ == '__main__':
    db = mysql.connector.connect(user="mesfin", passwd="tsme....",
                                 db="testdb", port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM person")
    states = cur.fetchall()

    for state in states:
        print(state)

    # host="localhost"
    # user="mesfin",
    # passwd="tsme....",
    # database="testdb"
