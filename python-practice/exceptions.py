x = 2

try:
    # print(x)
    if not type(x) is str:
        raise TypeError("Only strings are allowed")
except NameError:
    print('NameError is an error that occurs when there is use of an undefined vaiable')
except ZeroDivisionError:
    print('Please do not divide by zero')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error.")
