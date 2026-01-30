import sqlite3
from datetime import date

# --- DATABASE SETUP (The Pantry) ---
def init_db():
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, roll_no TEXT UNIQUE)')
    cursor.execute('CREATE TABLE IF NOT EXISTS attendance (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, date TEXT, status TEXT, FOREIGN KEY(student_id) REFERENCES students(id))')
    cursor.execute('CREATE TABLE IF NOT EXISTS subjects (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)')
    cursor.execute('CREATE TABLE IF NOT EXISTS marks (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, subject_id INTEGER, score REAL, FOREIGN KEY(student_id) REFERENCES students(id), FOREIGN KEY(subject_id) REFERENCES subjects(id))')
    
    # Pre-fill subjects if empty
    cursor.execute("SELECT COUNT(*) FROM subjects")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO subjects (name) VALUES (?)", [('Mathematics',), ('Physics',), ('Coding',)])
    
    conn.commit()
    conn.close()

# --- LOGIC FUNCTIONS (The Chef) ---

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    try:
        conn = sqlite3.connect('tracker.db')
        conn.execute("INSERT INTO students (name, roll_no) VALUES (?, ?)", (name, roll))
        conn.commit()
        print(f"✅ Student {name} added!")
    except sqlite3.IntegrityError:
        print("❌ Error: That Roll Number already exists!")
    finally:
        conn.close()

def mark_attendance():
    roll = input("Enter Roll Number: ")
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students WHERE roll_no = ?", (roll,))
    student = cursor.fetchone()
    
    if student:
        status = input(f"Marking {student[1]} (P/A): ").upper()
        if status in ['P', 'A']:
            cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)", 
                           (student[0], date.today().strftime("%Y-%m-%d"), status))
            conn.commit()
            print("✅ Attendance recorded.")
        else:
            print("❌ Invalid status. Use P or A.")
    else:
        print("❌ Student not found.")
    conn.close()

def enter_marks():
    roll = input("Enter Roll Number: ")
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students WHERE roll_no = ?", (roll,))
    student = cursor.fetchone()
    
    if student:
        cursor.execute("SELECT * FROM subjects")
        subs = cursor.fetchall()
        print("\nSubjects:")
        for s in subs: print(f"{s[0]}. {s[1]}")
        
        sub_id = input("Select Subject ID: ")
        try:
            score = float(input("Enter Score (0-100): "))
            cursor.execute("INSERT INTO marks (student_id, subject_id, score) VALUES (?, ?, ?)", 
                           (student[0], sub_id, score))
            conn.commit()
            print("✅ Marks saved.")
        except ValueError:
            print("❌ Error: Score must be a number.")
    else:
        print("❌ Student not found.")
    conn.close()

def generate_report():
    roll = input("Enter Roll Number for Analysis: ")
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students WHERE roll_no = ?", (roll,))
    student = cursor.fetchone()
    
    if not student:
        print("❌ Student not found.")
        return

    s_id, s_name = student
    
    # Calc Attendance
    cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id = ?", (s_id,))
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id = ? AND status = 'P'", (s_id,))
    present = cursor.fetchone()[0]
    att_pct = (present/total*100) if total > 0 else 0

    # Get Marks
    cursor.execute("SELECT subjects.name, marks.score FROM marks JOIN subjects ON marks.subject_id = subjects.id WHERE student_id = ?", (s_id,))
    marks = cursor.fetchall()

    print(f"\n--- PERFORMANCE REPORT: {s_name} ---")
    print(f"Attendance: {att_pct:.1f}%")
    print("Marks:")
    for m in marks: print(f"  > {m[0]}: {m[1]}")
    
    # Real-World Insight
    if att_pct < 75:
        print("⚠️ WARNING: Low attendance is hurting your eligibility!")
    if marks and all(m[1] < 40 for m in marks):
        print("⚠️ CRITICAL: Failing all subjects. Meeting with HOD recommended.")
    print("-" * 35)
    conn.close()

# --- MAIN MENU (The Dashboard) ---

def main():
    init_db()
    while True:
        print("\n=== STUDENT TRACKER SYSTEM ===")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Enter Marks")
        print("4. View Analytics")
        print("5. Exit")
        
        choice = input("Select Option: ")
        if choice == '1': add_student()
        elif choice == '2': mark_attendance()
        elif choice == '3': enter_marks()
        elif choice == '4': generate_report()
        elif choice == '5': break
        else: print("Invalid selection.")

if __name__ == "__main__":
    main()