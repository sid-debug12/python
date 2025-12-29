user = ['Sid', 'Moe', 'Lilly', 'Tom']
data = [19, 21, 18, 20]

empty = []
for i in range(len(user)):
    empty.append((user[i], data[i]))
    print(empty)

print("Dave" in user)
print(user[0])
print(user[-1])
print(user[-2])
print(user[0:2])
print(user[0:-2])
print(user[1:-1])

# Add a value in a list
print(len(user))

user.append("Dave")
print(user)

user += ["Anna", "Eva"]
print(user)

user.extend(["Sam", "Snow"])
print(user)

# user.extend(data)
# print(user)

# Inserting a value in a list

user.insert(1, "Bob")
print(user)

user[2:2] = ['Alpha', 'Beta']
print(user)


print(len(user))
print(user.count('Bob'))

# Remove a value in a list

user.remove('Bob')
print(user)

popped = user.pop()
print(popped)
print(user)

del user[-4:-3]
print(user)

data.clear()
print(data)

# Sorting a list

user[0:-2] = ['Sid']
user.sort()
print(user)
