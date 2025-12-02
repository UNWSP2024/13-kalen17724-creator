import sqlite3 

connection = sqlite3.connect("cities.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM cities")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
