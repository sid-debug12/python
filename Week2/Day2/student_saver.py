def save_students(filename, students):
    """Save students dictionary to file."""

    with open(filename, "w", encoding="utf-8") as file:
        for name, score in students.items():
            file.write(f"{name},{score}\n")
