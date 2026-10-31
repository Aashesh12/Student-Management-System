class Student:

    def __init__(self, student_id, name, email, department, semester, courses=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.department = department
        self.semester = semester
        self.courses = courses if courses is not None else {}

    def add_or_update_course(self, course_name, marks):
        self.courses[course_name] = marks

    def average(self):
        if not self.courses:
            return 0.0

        return sum(self.courses.values()) / len(self.courses)

    def grade(self):
        avg = self.average()

        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def status(self):
        return "Pass" if self.average() >= 50 else "Fail"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "semester": self.semester,
            "courses": self.courses
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["email"],
            data["department"],
            data["semester"],
            data.get("courses", {})
        )