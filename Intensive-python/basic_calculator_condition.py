# basic calculator with conditions

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operator = input("Choose operator [+,-,/,*] :")

if operator == '+':
    print(first_number + second_number)
elif operator == '-':
    print(first_number - second_number)
elif operator == '/':
    if second_number == 0:
        print("Error")
    else:
        print(first_number / second_number)
elif operator == '*':
    print(first_number * second_number)

else:
    print("Invalid operator")
