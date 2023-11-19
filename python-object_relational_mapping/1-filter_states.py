#!/usr/bin/python3
import MySQLdb
import sys


def list_states_starting_with_n(username, password, dbname):
    # Connect to the MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=dbname, host='localhost', port=3306)
    cursor = db.cursor()

    # Execute the query to fetch states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_starting_with_n(username, password, dbname)
