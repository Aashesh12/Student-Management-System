def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_student_id(prompt="Enter student ID: "):
    while True:
        value = input(prompt).strip()

        if not value:
            print("Student ID cannot be empty.")
        elif " " in value:
            print("Student ID cannot contain spaces.")
        else:
            return value


def get_email(prompt="Enter email: "):
    while True:
        email = input(prompt).strip()

        if "@" in email and "." in email.split("@")[-1] and " " not in email:
            return email

        print("Please enter a valid email address.")


def get_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt).strip())

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must be at most {maximum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid whole number.")


def get_marks(prompt="Enter marks (0-100): "):
    return get_integer(prompt, 0, 100)