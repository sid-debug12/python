# Remove all zeros
numbers = []
size = int(input("Enter the length of the list: "))
print("Enter the numbers: ")

for i in range(size):
    number = int(input())
    numbers.append(number)

# Remove ALL zeros
numbers = [num for num in numbers if num != 0]

print(f"List after removing zeros: {numbers}")
