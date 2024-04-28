import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('database/DINERS.db')
c = conn.cursor()

# Create the CANTEEN table
c.execute('''
    CREATE TABLE CANTEEN
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Location TEXT NOT NULL,
    time_open TEXT NOT NULL,
    time_closed TEXT NOT NULL);
''')

# Open the CSV file and insert the data into the CANTEEN table
with open('database/Canteens.csv', 'r', encoding='utf-8') as fin:
    csv_reader = csv.reader(fin, delimiter=';')
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        name, location, _, open_time = row
        time_open, time_closed = open_time.split('-')
        c.execute("INSERT INTO CANTEEN (Name, Location, time_open, time_closed) VALUES (?, ?, ?, ?);",
                  (name, location, time_open, time_closed))

# Commit the changes and close the connection
conn.commit()
conn.close()