"""Program for combining two different files and if have same info as one file will sum the results"""

# Declaration of values

item_names = []
item_values = []

with open("file1.txt", encoding="utf-8") as file:
    for line in file:
        name, value = line.rstrip("\n").split("=")
        item_names.append(name)
        item_values.append(int(value))

item1_names = []
item1_values = []

with open("file1.txt", encoding="utf-8") as file:
    for line in file:
        name, value = line.rstrip("\n").split("=")
        item1_names.append(name)
        item1_values.append(int(value))

item2_names = []
item2_values = []

for i in range(len(item_names)):
    if item_names[i] in item2_names:
        j = item2_names.index(item_names[i])
        item2_values[j] += item_values[i]
    else:
        item2_names.append(item_names[i])
        item2_values.append(item_values[i])

for i in range(len(item1_names)):
    if item_names[i] in item2_names:
        j = item2_names.index(item1_names[i])
        item2_values[j] += item1_values[i]
    else:
        item2_names.append(item1_names[i])
        item2_values.append(item1_values[i])

with open('output.txt', 'w') as file:
    for i in range(len(item2_names)):
        file.write("{}={}\n".format(item2_names[i], item2_values[i]))
