# Login system

correct_username = "Siegfried"
correct_password = "PythonMaster"

username = input("Enter your login system name: ")
password = input("Enter your login user password: ")

if username == correct_username and password == correct_password:
    print("Access granted")

else:
    print("Access denied")
