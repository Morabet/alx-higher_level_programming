#!/usr/bin/python3

"""
python script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    name = argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=name, charset="utf8")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    sql_query = "SELECT cities.id, cities.name, states.name FROM cities \
JOIN states ON states.id = cities.state_id"

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
