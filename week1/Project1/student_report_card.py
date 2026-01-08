names = []
scores = []

size = int(input("Number of students: "))
print("Enter the names of students: ")
for i in range(size):
    name = input("")
    names.append(name)

print("Enter the scores: ")

for i in range(size):
    while True:
        score = int(input(""))
        if score >= 0 and score <= 100:
            scores.append(score)
            break
        print("score should between 0 and 100")

largest_score = max(scores)
average_score = sum(scores) / len(scores)

for i in range(size):
    print(f"Student: {names[i]}, Score: {scores[i]}")

print(f"Largest score: {largest_score}")
print(f"Average score: {average_score}")
