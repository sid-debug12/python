# def hello():
#     print("hello world")


# hello()


# def add(x, y):
#     """Return the sum of x and y."""
#     return x + y


# Get user input
# x = float(input("Enter the first number: "))
# y = float(input("Enter the second number: "))

# print(add(x, y))
#  when we don't know how many parameters will be passed in


def add_all(*args):
    """Return the sum of all arguments passed."""
    total = 0
    for arg in args:
        total += arg
    return total


numbers = input("Enter numbers separated by spaces: ")
if numbers.strip():
    num_list = [float(n) for n in numbers.split()]
    print(add_all(*num_list))
else:
    print("No numbers entered.")
