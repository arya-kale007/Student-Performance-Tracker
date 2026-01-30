import sqlite3

conn = sqlite3.connect('tracker.db')
cursor = conn.cursor()

# 1. Create Subjects table (e.g., Math, Physics, Coding)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
''')

# 2. Create Marks table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS marks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        score REAL,
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (subject_id) REFERENCES subjects (id)
    )
''')

# 3. Add some default subjects to get started
subjects = [('Mathematics',), ('Physics',), ('Python Programming',), ('Chemistry',), ('Biology for Engineers',)]
cursor.executemany("INSERT OR IGNORE INTO subjects (name) VALUES (?)", subjects)

conn.commit()
conn.close()
print("Performance tables ready and subjects populated!")