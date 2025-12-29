# Exercise A - Student Registry (Corrected)

students = {}

size = int(input("Enter the number of students: "))
print("Fill in the students names and scores:")

for _ in range(size):
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
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")

print("\nStudent Registry:")
for name, score in students.items():
    print(f"{name:<15} {score:>5}")
