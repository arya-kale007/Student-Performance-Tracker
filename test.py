import sqlite3

# 1. Connect to a database file (it will create it if it doesn't exist)
connection = sqlite3.connect('my_college.db')

# 2. Get a 'cursor' (think of this as a pen we use to write)
cursor = connection.cursor()

# 3. Write a command to create a 'Students' table
cursor.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, roll_no TEXT)')

print("Success! You just built the 'Pantry' (Database).")
connection.close()
