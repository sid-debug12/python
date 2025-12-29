value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equal to " + str(value))

for x in names:
    print(x)

for x in "Yaounde":
    print(x)

for x in names:
    if x == "Paul":
        break
    print(x)

for x in names:
    if x == "Paul":
        continue
    print(x)

for x in range(4):
    print(x)

for x in range(2, 4):
    print(x)

for x in range(5, 101, 5):
    print(x)
else:
    print("Glad that\'s over!")

names = ["John", "Paul", "George"]
actions = ["jump", "run", "sit"]

for name in names:
    for action in actions:
        print(name + " wants to " + action)

for action in actions:
    for name in names:
        print(name + " wants to " + action)
