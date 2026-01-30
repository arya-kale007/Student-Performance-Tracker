import sqlite3

def add_marks():
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()

    # 1. Find Student
    roll = input("Enter Student Roll Number: ")
    cursor.execute("SELECT id, name FROM students WHERE roll_no = ?", (roll,))
    student = cursor.fetchone()
    
    if not student:
        print("Student not found!")
        return

    # 2. Show Subjects
    print("\nAvailable Subjects:")
    cursor.execute("SELECT * FROM subjects")
    subs = cursor.fetchall()
    for s in subs:
        print(f"{s[0]}. {s[1]}")
    
    sub_id = input("\nEnter Subject ID: ")
    score = float(input(f"Enter marks for {student[1]}: "))

    # 3. Save
    cursor.execute("INSERT INTO marks (student_id, subject_id, score) VALUES (?, ?, ?)", 
                   (student[0], sub_id, score))
    
    conn.commit()
    print(f"✅ Marks saved for {student[1]}!")
    conn.close()

add_marks()