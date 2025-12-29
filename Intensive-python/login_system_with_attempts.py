# login system with 3 attempts

attempt = 3
count = 0

correct_username = "Siegfried"
correct_password = "PythonMaster"

while count < attempt:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Access granted")
        break

    else:
        print("Access denied")
        count += 1

        if count < attempt:
            print(f"Attempts remaining: {attempt - count}")


if count == attempt:
    print("Account Locked")
