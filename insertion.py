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

def select_from_db():
	
	# select entire table
	cursor.execute("SELECT * FROM people")
	
	# in form of a list of tuples representing each row
	data = cursor.fetchall()

	# print every row in selection
	for row in data:
		# each row is a tuple
		print row

	# select specific column(s) from table
	cursor.execute("SELECT Age FROM people")
	data = cursor.fetchall()
	
	# print each observed age
	print "Observed ages: "
	for row in data:
		print row[0]

# Create table and make entry
create_table()

# Insert 10 Edward's with random ages
for i in range(10):
	insert_random_me(i)

# Commit changes
conn.commit()

# Select
select_from_db()

# Close cursor and connection
cursor.close()
conn.close()



