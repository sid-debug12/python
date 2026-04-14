"""Module that reads a file and calculates sum and average of numbers."""

# Corrected version


def file_reading(filename):
    """Read numbers from file and return sum and average."""
    total = 0
    count = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            number = int(line.strip())
            total += number
            count += 1

    if count == 0:
        raise ValueError("File is empty")

    average = total / count

    return total, average
