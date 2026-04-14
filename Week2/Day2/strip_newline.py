import sys
filename = sys.argv[0]
with open(filename, encoding='utf-8') as file:
    lines = []
    for line in file:
        lines.append(line.rstrip("\n"))
    print(lines)
