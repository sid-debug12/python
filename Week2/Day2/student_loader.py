def load_students(filename):
    students = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                name, score = line.strip().split(",")
                students[name.strip()] = int(score.strip())
    except FileNotFoundError:
        pass

    return students
