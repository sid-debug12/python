"""Module to read and print numbers from a file."""

filename = 'number.txt'
count = [0] * 10
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        for i in line.rstrip("\n"):
            if i == ' ':
                continue
            i = int(i)
            count[i] += 1
for i in range(10):
    print("{} {}".format(i, count[i]))
