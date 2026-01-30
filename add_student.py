import sqlite3

def add_student_to_db(name, roll_no):
    # 1. Open the warehouse door (Connect)
    connection = sqlite3.connect('tracker.db')
    cursor = connection.cursor()

    # 2. Prepare the command (The '?' are placeholders for safety)
    sql_command = "INSERT INTO students (name, roll_no) VALUES (?, ?)"
    
    # 3. Execute the command with our data
    cursor.execute(sql_command, (name, roll_no))

    # 4. LOCK IN the changes (This is called a 'commit')
    connection.commit()

    # 5. Close the door
    connection.close()
    print(f"Success! {name} has been added to the system.")

# --- Execution ---
# Let's actually use the function now
user_name = input("Enter student name: ")
user_roll = input("Enter roll number: ")

add_student_to_db(user_name, user_roll)