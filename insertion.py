import sqlite3
import random 

# Create a connection and a cursor
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Function to create a static table
def create_table():
	cursor.execute("CREATE TABLE IF NOT EXISTS people(ID INTEGER PRIMARY KEY, Name TEXT, Age REAL);")

# Function to make a static insertion
def insert_me():
	cursor.execute("INSERT INTO people Values(1,'Edward Butler', 19)")
	conn.commit()
	cursor.close()
	conn.close()

def insert_random_me(id):
	random_age = random.randrange(100)
	cursor.execute("INSERT INTO people (ID, Name, Age) Values (?,?,?)", (id, "Edward Butler", random_age))


# Create table and make entry
create_table()

# Insert 10 Edward's with random ages
for i in range(10):
	insert_random_me(i)

# Commit changes
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()



