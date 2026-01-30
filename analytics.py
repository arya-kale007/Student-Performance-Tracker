import sqlite3

def get_final_report(roll_no):
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()

    # Get Student Info
    cursor.execute("SELECT id, name FROM students WHERE roll_no = ?", (roll_no,))
    student = cursor.fetchone()
    if not student: return print("Not found.")
    
    s_id, s_name = student

    # --- Part A: Attendance Logic ---
    cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id = ?", (s_id,))
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id = ? AND status = 'P'", (s_id,))
    present = cursor.fetchone()[0]
    att_pct = (present/total*100) if total > 0 else 0

    # --- Part B: Performance Logic ---
    cursor.execute('''
        SELECT subjects.name, marks.score 
        FROM marks 
        JOIN subjects ON marks.subject_id = subjects.id 
        WHERE marks.student_id = ?
    ''', (s_id,))
    marks_data = cursor.fetchall()

    # --- Part C: The "Smart" Output ---
    print(f"\n{'='*40}")
    print(f"ENGINEERING REPORT: {s_name.upper()}")
    print(f"{'='*40}")
    print(f"ATTENDANCE: {att_pct:.1f}%")
    
    print("\nACADEMIC PERFORMANCE:")
    if not marks_data:
        print("- No marks recorded yet.")
    else:
        for sub, score in marks_data:
            status = "PASS" if score >= 40 else "FAIL"
            print(f"  > {sub}: {score} [{status}]")

    # --- Part D: Real-World Insight ---
    if att_pct < 75 and any(m[1] < 40 for m in marks_data):
        print("\nANALYSIS: Low attendance is likely impacting performance.")
    elif att_pct < 75:
        print("\nANALYSIS: Performance is okay, but you are at risk of debarment.")
    
    print(f"{'='*40}\n")
    conn.close()

r = input("Enter Roll Number for Final Analysis: ")
get_final_report(r)
