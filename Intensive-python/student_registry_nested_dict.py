
"""Student registry system with grading and performance tracking."""

size = int(input("Enter the number of students: "))
print("Fill in the students names: ")
students = {}

for i in range(size):
    while True:
        name = input("Name: ").strip()
        if name == "":
            print("Name cannot be empty.")
        elif name in students:
            print("Student already exists.")
        else:
            break
    while True:
        try:
            score = float(input("Score: "))
            if 0 <= score <= 100:
                students[name] = score
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")
# check if there are students to avoid errors in statistics calculation
if not students:
    print("No students in the registry. Exiting program.")
    exit()

# Grading and status of students performance
for name, score in students.items():
    if score >= 80:
        grade = 'A'
        status = "Pass"
    elif 70 <= score < 80:
        grade = 'B'
        status = "Pass"
    elif 60 <= score < 70:
        grade = 'C'
        status = "Pass"
    elif 50 <= score < 60:
        grade = 'D'
        status = "Pass"
    else:
        grade = 'F'
        status = "Fail"
    students[name] = {
        'score': score,
        'grade': grade,
        'status': status
    }

# Display results
print(f"{'Name':<15} {'Score':<15} {'Status':<15} {'Grade':>5}")
print("-" * 55)
for name, data in students.items():
    print(
        f"{name:<15} {data['score']:<15} {data['status']:<15} {data['grade']:>5}")

    # while True:
    #     name = input("Name: ").strip()
    #     if name == "":
    #         print("Name cannot be empty.")
    #     elif name in students:
    #         print("Student already exists.")
    #     else:
    #         break

    # while True:6
    #     try:
    #         score = float(input("Score: "))
    #         if 0 <= score <= 100:
    #             students[name] = score
    #             break
    #         else:
    #             print("Score must be between 0 and 100.")
    #     except ValueError:
    #         print("Invalid input. Enter a number.")
