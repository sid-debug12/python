def even_odd(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    return "Even" if number % 2 == 0 else "Odd"
