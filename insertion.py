import sqlite3

# Create a connection and a cursor
conn = sqlite3.connect('staticData.db')
cursor = conn.cursor()

# Function to create a static table
def create_table():
	cursor.execute("CREATE TABLE IF NOT EXISTS people(ID INTEGER PRIMARY KEY, Name TEXT);")

# Function to make a static insertion
def insert_person():
	cursor.execute("INSERT INTO people Values(1,'Edward Butler')")
	conn.commit()
	cursor.close()
	conn.close()

# Create table and make entry
create_table()
insert_person()



