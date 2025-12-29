# pass fail program

while True:
    score = float(input("Enter your score between [0, 100]: "))
    if score >= 0 and score <= 100:
        break

if score < 50:
    print("Fail")
else:
    print("Pass")
