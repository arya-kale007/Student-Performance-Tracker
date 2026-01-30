import sqlite3

connection = sqlite3.connect('tracker.db')
cursor = connection.cursor()

# Get everything from the students table
cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()

print("Current Students in Database:")
for student in all_students:
    print(student)

connection.close()