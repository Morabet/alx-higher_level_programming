#!/usr/bin/python3

""" python script that lists all states from the database
hbtn_0e_0_usa with a given name
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    name = argv[3]
    searched = argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=name, charset="utf8")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    sql_query = "SELECT id, name FROM states "
    sql_query += "WHERE name = '{}' ORDER BY id;".format(searched)

    try:
        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all the rows
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and the database connection
        cursor.close()
        db.close()
