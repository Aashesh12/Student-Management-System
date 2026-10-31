from student import Student
from student_manager import StudentManager

from validators import (
    get_email,
    get_integer,
    get_marks,
    get_non_empty,
    get_student_id
)


def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def pause():
    input("\nPress Enter to continue...")


def display_student(student):

    print("\n" + "-" * 60)

    print(f"Student ID : {student.student_id}")
    print(f"Name       : {student.name}")
    print(f"Email      : {student.email}")
    print(f"Department : {student.department}")
    print(f"Semester   : {student.semester}")

    print("\nCourses:")

    if student.courses:

        for course, marks in student.courses.items():
            print(f"  - {course}: {marks}")

    else:
        print("  No course marks entered.")

    print(f"\nAverage    : {student.average():.2f}")
    print(f"Grade      : {student.grade()}")
    print(f"Status     : {student.status()}")

    print("-" * 60)


def add_student(manager):

    print_header("ADD STUDENT")

    student_id = get_student_id()

    if manager.find_by_id(student_id):
        print("A student with this ID already exists.")
        return

    name = get_non_empty("Enter name: ")

    email = get_email()

    department = get_non_empty("Enter department: ")

    semester = get_integer(
        "Enter semester (1-8): ",
        1,
        8
    )

    student = Student(
        student_id,
        name,
        email,
        department,
        semester
    )

    if manager.add_student(student):
        print("Student added successfully.")
    else:
        print("Could not add student.")


def view_all_students(manager):

    print_header("ALL STUDENTS")

    if not manager.students:
        print("No students found.")
        return

    print(
        f"{'ID':<12}"
        f"{'Name':<22}"
        f"{'Department':<18}"
        f"{'Sem':<5}"
        f"{'Avg':<8}"
    )

    print("-" * 65)

    for student in manager.students:

        print(
            f"{student.student_id:<12}"
            f"{student.name[:20]:<22}"
            f"{student.department[:16]:<18}"
            f"{student.semester:<5}"
            f"{student.average():<8.2f}"
        )


def search_students(manager):

    print_header("SEARCH STUDENTS")

    keyword = get_non_empty(
        "Enter ID, name, or department: "
    )

    results = manager.search(keyword)

    if not results:
        print("No matching students found.")
        return

    print(f"Found {len(results)} student(s).")

    for student in results:

        print(
            f"- {student.student_id} | "
            f"{student.name} | "
            f"{student.department} | "
            f"Semester {student.semester}"
        )


def view_student(manager):

    print_header("VIEW STUDENT")

    student_id = get_student_id()

    student = manager.find_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    display_student(student)


def update_student(manager):

    print_header("UPDATE STUDENT")

    student_id = get_student_id()

    student = manager.find_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    print(
        "Leave a text field blank "
        "to keep the current value."
    )

    name = input(
        f"Name [{student.name}]: "
    ).strip()

    email = input(
        f"Email [{student.email}]: "
    ).strip()

    department = input(
        f"Department [{student.department}]: "
    ).strip()

    semester_text = input(
        f"Semester [{student.semester}]: "
    ).strip()

    if name:
        student.name = name

    if email:

        if (
            "@" in email
            and "." in email.split("@")[-1]
            and " " not in email
        ):
            student.email = email

        else:
            print(
                "Invalid email. "
                "Existing email was kept."
            )

    if department:
        student.department = department

    if semester_text:

        try:

            semester = int(semester_text)

            if 1 <= semester <= 12:
                student.semester = semester
            else:
                print(
                    "Semester must be between "
                    "1 and 12. Existing value kept."
                )

        except ValueError:

            print(
                "Invalid semester. "
                "Existing value kept."
            )

    manager.save()

    print("Student updated successfully.")


def delete_student(manager):

    print_header("DELETE STUDENT")

    student_id = get_student_id()

    student = manager.find_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    print(
        f"Student: {student.name} "
        f"({student.student_id})"
    )

    confirmation = input(
        "Type YES to delete: "
    ).strip()

    if confirmation == "YES":

        if manager.delete_student(student_id):
            print("Student deleted successfully.")

    else:
        print("Deletion cancelled.")


def add_course_marks(manager):

    print_header("ADD / UPDATE COURSE MARKS")

    student_id = get_student_id()

    student = manager.find_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    course = get_non_empty(
        "Enter course name: "
    )

    marks = get_marks()

    student.add_or_update_course(
        course,
        marks
    )

    manager.save()

    print(
        f"Marks saved: {course} = {marks}"
    )

    print(
        f"Current average: "
        f"{student.average():.2f}"
    )

    print(
        f"Current grade: "
        f"{student.grade()}"
    )


def show_statistics(manager):

    print_header("CLASS STATISTICS")

    stats = manager.statistics()

    print(
        f"Total students : "
        f"{stats['total']}"
    )

    print(
        f"Class average  : "
        f"{stats['average']:.2f}"
    )

    print(
        f"Passed         : "
        f"{stats['passed']}"
    )

    print(
        f"Failed         : "
        f"{stats['failed']}"
    )


def show_menu():

    print_header("STUDENT MANAGEMENT SYSTEM")

    print("1. Add student")
    print("2. View all students")
    print("3. Search students")
    print("4. View student details")
    print("5. Update student")
    print("6. Delete student")
    print("7. Add / update course marks")
    print("8. Class statistics")
    print("0. Exit")


def main():

    manager = StudentManager()

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            add_student(manager)

        elif choice == "2":
            view_all_students(manager)

        elif choice == "3":
            search_students(manager)

        elif choice == "4":
            view_student(manager)

        elif choice == "5":
            update_student(manager)

        elif choice == "6":
            delete_student(manager)

        elif choice == "7":
            add_course_marks(manager)

        elif choice == "8":
            show_statistics(manager)

        elif choice == "0":

            print(
                "\nThank you for using "
                "Student Management System."
            )

            break

        else:
            print(
                "Invalid choice. "
                "Please select a menu option."
            )

        pause()


if __name__ == "__main__":
    main()