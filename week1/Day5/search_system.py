# search system

students = ["Siegfried", "Anna", "Mark", "Peter", "Linda"]

search_name = input("Enter the name to search: ")

found = False
for student in students:
    if search_name == student:
        found = True
        break
if found == True:
    print("Found")

if found != True:
    print("Not Found")


# Alternative approach using while loop

students = ["Siegfried", "Anna", "Mark", "Peter", "Linda"]
search_name = input("Enter the name to search: ")
count = 0

found = False
while count < len(students):
    if search_name == students[count]:
        found = True
        break
    count += 1

if found == True:
    print("Found")

if found != True:
    print("Not Found")
