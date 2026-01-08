# Even Odd Seperator

numbers = [10]

print("Enter ten numbers: ")
for i in range(10):
    number = int(input(""))
    numbers.append(number)
even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
