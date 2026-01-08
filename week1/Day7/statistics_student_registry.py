"""Exercise B: Student Registry Statistics"""
students = {}
size = int(input("Enter the number of students: "))
print("Fill in the students names and scores:")

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

# Check if there are students to avoid errors in statistics calculation
if not students:
    print("No students in the registry. Exiting program.")
    exit()

# Calculate statistics
scores_iterator = iter(students.values())
first_score = next(scores_iterator)
lowest_score = first_score
highest_score = first_score
total_score = first_score
count = 1

for score in scores_iterator:
    if score < lowest_score:
        lowest_score = score
    if score > highest_score:
        highest_score = score
    total_score += score
    count += 1
average_score = total_score / count

# Display results
print("Student Registry:")
for name, score in students.items():
    print(f"{name:<15} {score:>5}")
print(f"Lowest Score: {lowest_score}")
print(f"Highest Score: {highest_score}")
print(f"Average Score: {average_score:.2f}")

# REQUIRED IMPROVEMENTS (conceptual, not full rewrite)
# You should add:
# 1. A guard before statistics:
# If students is empty → print a message and exit
# 2. Formatted output
# Loop through students.items() neatly
# 3. Clearer iterator naming
