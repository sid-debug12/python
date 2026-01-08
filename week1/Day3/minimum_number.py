number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))

smallest = number1

if smallest >= number2:
    smallest = number2

if smallest >= number3:
    smallest = number3

if smallest >= number4:
    smallest = number4

print(f"The smallest number is: {smallest}")
