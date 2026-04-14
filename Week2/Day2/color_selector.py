def main():
    try:
        with open('color.txt', encoding="utf-8") as file:
            colors = []
            for line in file:
                colors.append(line.rstrip("\n"))
    except IOError:
        print("Could not open colors.txt")
        exit()

    for i in range(len(colors)):
        print("{} {}".format(i, colors[i]))

    print(colors[input("Select color: ")])


main()
