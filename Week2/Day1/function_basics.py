students = {
    "Alice": 78,
    "Bob": 92,
    "Charlie": 65
}


def print_students(students):
    for names, scores in students.items():
        print(f"{names:<15} -> {scores:>5}")


print_students(students)
