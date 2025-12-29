# List analyser

numbers = []
print("Enter five numbers: ")
for i in range(5):
    number = int(input(""))
    numbers.append(number)

largest = max(numbers)
smallest = min(numbers)
total = sum(numbers)

print(f"The list {numbers}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of numbers: {total}")
