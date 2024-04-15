class AttendanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student not in self.students:
            self.students[student] = [student, False]
        else:
            raise ValueError

    def check_in(self, student):
        # self.students[student] = [student, True]
        self.students[student][-1]=True

    def delete_student(self, student):
        if student in self.students:
            # del self.students[student]
            self.students.pop(student)
        else: raise ValueError