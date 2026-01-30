import sqlite3
from datetime import date

def mark_attendance():
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()

    # 1. Ask for ROLL NUMBER (Easier for humans)
    roll = input("Enter Student Roll Number: ")
    
    # 2. Find the hidden Database ID for that Roll Number
    cursor.execute("SELECT id, name FROM students WHERE roll_no = ?", (roll,))
    student = cursor.fetchone()

    if student is None:
        print(f"❌ Error: No student found with Roll Number '{roll}'")
        conn.close()
        return

    student_id = student[0]
    student_name = student[1]

    # 3. Get status
    status = input(f"Marking {student_name}. Enter Status (P/A): ").upper()
    today = date.today().strftime("%Y-%m-%d")

    # 4. Save it
    cursor.execute('''
        INSERT INTO attendance (student_id, date, status) 
        VALUES (?, ?, ?)
    ''', (student_id, today, status))
    
    conn.commit()
    print(f"✅ Success: {student_name} marked {status} for {today}.")
    
    conn.close()

mark_attendance()