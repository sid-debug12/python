from random import choice

bird = "Western Meadowlark"
flower = "Sunflower"
song = "Perfect"
capital = "Topeka"


def randomfunfact():
    funfacts = [
        "Cans is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Cans city.",
        "A considerable portion of Cans city is actually in Missouri"
    ]

    index = choice("012")
    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()
