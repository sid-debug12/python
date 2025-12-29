
# format for a recursive statement in python

# def recursive_function(args):
#     if base_case_condition:
#         return base_case_value
#     else:
#         # reduce the problem and call itself
#         return recursive_function(smaller_problem)

# """This module provides a recursive function to add one to a number until it exceeds 10."""


# def add_one(x):
#     """Recursively adds one to x and prints each step until x exceeds 10."""
#     if x <= 10:
#         total = x + 1
#         print(total)
#         return add_one(total)
#     return x


# print(add_one(0))

def add_num(x):
    """Recursively adds one to x and prints each step until x exceeds 10."""
    if x >= 11:
        return x + 1
    total = x + 1
    print(total)

    return add_num(total)


result = add_num(1)
print(result)
