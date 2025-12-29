import argparse

parser = argparse.ArgumentParser(
    description="Personalized CLI greeting tool."
)

# --name argument
parser.add_argument(
    "-n", "--name", metavar="name", required=True,
    help="The name of the person."
)

# --age argument
parser.add_argument(
    "-a", "--age", metavar="age", type=int,
    help="The age of the person"
)

# --language argument
parser.add_argument(
    "-l", "--language", metavar="lang", choices=["en", "fr", "es"],
    default="en", help="language for the greeting (en, fr, es)"
)

# --shout argument
parser.add_argument(
    "-s", "--shout", action="store_true",
    help="If set, the greeting will be in uppercase."
)

args = parser.parse_args()

# greeting logic

greetings = {
    "en": "Hello",
    "fr": "Bonjour",
    "es": "Hola"
}

msg = f"{greetings[args.language]}, {args.name}!"

if args.age:
    msg += f"you are {args.age} years old."

if args.shout:
    msg = msg.upper()

print(msg)
