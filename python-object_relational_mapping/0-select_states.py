#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa

"""


import MySQLdb
from sys import argv


def list_states(username, password, dbname):
    db = MySQLdb.connect(user=username, passwd=password, db=dbname, host='localhost', port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC;"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, dbname)
