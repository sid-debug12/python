person = "Sid"
coins = 3

# message = f"\n{person} has {coins} coins left."
# print(message)

# message = f"\n{person} has {10 * 4} coins left."
# print(message)

# message = f"\n{person.lower()} has {10 * 4} coins left."
# print(message)
print("\n" + person + " has " + str(coins) + " coins left.")
message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(
    person=person, coins=coins)
print(message)

player = {'person': 'Dave', 'coins': '10'}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {10 * 4} coins left."
print(message)

message = f"\n{person.lower()} has {10 * 4} coins left."
print(message)

message = f"\n{player['person']} has {player['coins']} coins left."
print(message)

############################
# pass formating options that can help in placing decimal places

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}.")
print(f"\n2.25 times {num} is {2.25 * num:.3f}.")

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}.")

for num in range(1, 11):
    print(f"\n{num} divided by 4.52 is {num / 4.52:.2%}.")
