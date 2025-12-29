name = "Sid"  # global scope
count = 1


def another():

    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):

        print(name)
        color = "red"  # local scope
        print(color)

    greeting("Kim")


another()
