def validate_students(students):

    students_dict = []

    for name, score in students.items():

        if not isinstance(score, (int, float)):
            raise ValueError("Score must be a number")
        if not (0 <= score <= 100):
            raise ValueError("Score is not in range")
        students_dict.append(f"{name} {score}")
        return students
