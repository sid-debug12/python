# number sign checker

times = int(input("How many times do you want to check a number? "))

count = 0
while count < times:
    number = float(input("Enter a number: "))

    if number > 0:
        print("Positive")

    elif number < 0:
        print("Negative")

    else:
        print("Zero")
    count += 1
