class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Student(User):
    def __init__(self, user_id, name, roll_no):
        super().__init__(user_id, name)
        self.roll_no = roll_no

class Teacher(User):
    def __init__(self, user_id, name, subject):
        super().__init__(user_id, name)
        self.subject = subject