"""Simple text-based menu to collect names into a table.

Usage:
- Run: `python menu_interface.py`
- Choose option `1` to add a name, `2` to show the table, `3` to exit.

This keeps data in memory for the session. If you'd like persistence
I can add CSV/JSON save/load options.
"""


def display_menu():
    print("\n=== Simple Menu ===")
    print("1. Add name")
    print("2. Show table")
    print("3. Exit")


def add_name(table):
    name = input("Enter name: ").strip()
    if not name:
        print("No name entered. Nothing was added.")
        return
    table.append({"name": name})
    print(f"Added: {name}")


def show_table(table):
    if not table:
        print("No entries yet.")
        return

    # compute column widths
    idx_width = max(len(str(len(table))), 2)
    name_width = max(max((len(row['name']) for row in table), default=4), 4)

    header = str('#').rjust(idx_width) + '  ' + 'Name'.ljust(name_width)
    sep = '-' * (idx_width + 2 + name_width)
    print('\n' + header)
    print(sep)
    for i, row in enumerate(table, 1):
        print(str(i).rjust(idx_width) + '  ' + row['name'].ljust(name_width))
    print()


def main():
    table = []
    while True:
        display_menu()
        choice = input("Choose (1-3): ").strip()
        if choice == '1':
            add_name(table)
        elif choice == '2':
            show_table(table)
        elif choice == '3':
            print("Exiting. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == '__main__':
    main()
