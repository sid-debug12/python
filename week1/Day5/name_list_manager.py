# Name list manager

names = []
size = int(input("Enter the number of names you want to enter: "))
print("Enter the names: ")

for i in range(size):
    name = input("")
    names.append(name)

print(f"The full list {names}")
print(f"The first name {names[0]}")
print(f"The last name {names[-1]}")
print(f"List in alphabetical order {sorted(names)}")
