from student import Student
from storage import load_students, save_students


class StudentManager:
    """Handles CRUD operations and searching for students."""

    def __init__(self):
        self.students = []
        self.load()

    def load(self):
        data = load_students()

        self.students = [
            Student.from_dict(item)
            for item in data
        ]

    def save(self):
        return save_students(
            [student.to_dict() for student in self.students]
        )

    def find_by_id(self, student_id):
        for student in self.students:
            if student.student_id.lower() == student_id.lower():
                return student

        return None

    def add_student(self, student):
        if self.find_by_id(student.student_id):
            return False

        self.students.append(student)
        self.save()

        return True

    def delete_student(self, student_id):
        student = self.find_by_id(student_id)

        if student is None:
            return False

        self.students.remove(student)
        self.save()

        return True

    def search(self, keyword):
        keyword = keyword.lower()

        return [
            student
            for student in self.students
            if keyword in student.student_id.lower()
            or keyword in student.name.lower()
            or keyword in student.department.lower()
        ]

    def statistics(self):
        if not self.students:
            return {
                "total": 0,
                "average": 0.0,
                "passed": 0,
                "failed": 0
            }

        averages = [
            student.average()
            for student in self.students
        ]

        passed = sum(
            1
            for student in self.students
            if student.status() == "Pass"
        )

        return {
            "total": len(self.students),
            "average": sum(averages) / len(averages),
            "passed": passed,
            "failed": len(self.students) - passed
        }