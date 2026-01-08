def search_student(students_table):
    search_name = input("Enter name to search: ").lower()
    found = False

    for row in students_table:
        if row[1].lower() == search_name:
            print(f"Found → No: {row[0]}, Name: {row[1]}, Score: {row[2]}")
            found = True
            break

    if not found:
        print("Student not found.")
