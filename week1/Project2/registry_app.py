# TO run program: python registry_app.py. Run uvicorn main:app --reload in bash to start FastAPI server

"""
Mini Project: Student Registry System (OOP Version)
Author: Siegfried
Description:
- Add, search, sort students
- Show statistics
- Persistent storage using JSON
"""

import json
import os
from fastapi import FastAPI
import sqlite3

# ---------------- STORAGE LAYER ---------------- #

app = FastAPI()


@app.get("/students")
def get_students():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    return dict(cur.fetchall())


class database:
    FILE_NAME = "students.json"

    @staticmethod
    def load():
        if not os.path.exists(database.FILE_NAME):
            return {}

        try:
            with open(database.FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error loading file. Starting fresh.")
            return {}

    @staticmethod
    def save(data):
        with open(database.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)


# ---------------- CORE LOGIC ---------------- #

class StudentRegistry:
    def __init__(self):
        self.students = database.load()

    def add_students(self):
        size = int(input("Enter number of students to add: "))

        for _ in range(size):
            while True:
                name = input("Name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                elif name in self.students:
                    print("Student already exists.")
                else:
                    break

            while True:
                try:
                    score = float(input("Score: "))
                    if 0 <= score <= 100:
                        self.students[name] = score
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input.")

        database.save(self.students)
        print("Students saved successfully.")

    def display(self):
        if not self.students:
            print("No students in registry.")
            return

        print(f"\n{'Name':<15} {'Score':>5}")
        print("-" * 22)
        for name, score in self.students.items():
            print(f"{name:<15} {score:>5}")

    def statistics(self):
        if not self.students:
            print("No students available.")
            return

        scores = list(self.students.values())
        print(f"Lowest Score : {min(scores)}")
        print(f"Highest Score: {max(scores)}")
        print(f"Average Score: {sum(scores)/len(scores):.2f}")

    def search(self):
        name = input("Enter student name to search: ").strip()
        for student in self.students:
            if student.lower() == name.lower():
                print(f"{student} → Score: {self.students[student]}")
                return
        print("Student not found.")

    def sort_students(self):
        if not self.students:
            print("No students to sort.")
            return

        print("1. Sort by name")
        print("2. Sort by score (highest first)")
        choice = input("Choose option: ")

        if choice == '1':
            sorted_students = dict(sorted(self.students.items()))
        elif choice == '2':
            sorted_students = dict(
                sorted(self.students.items(), key=lambda x: x[1], reverse=True)
            )
        else:
            print("Invalid choice.")
            return

        print("\nSorted Students:")
        for name, score in sorted_students.items():
            print(f"{name:<15} {score:>5}")

    def update_student(self):
        name = input("Enter student name to update: ").strip()
        if name not in self.students:
            print("Student not found.")
            return

        try:
            new_score = float(input("Enter new score: "))
            if 0 <= new_score <= 100:
                self.students[name] = new_score
                database.save(self.students)
                print("Student updated.")
            else:
                print("Invalid score range.")
        except ValueError:
            print("Invalid input.")

    def delete_student(self):
        name = input("Enter student name to delete: ").strip()
        if name in self.students:
            del self.students[name]
            database.save(self.students)
            print("Student deleted.")
        else:
            print("Student not found.")


# ---------------- APPLICATION LAYER ---------------- #

class StudentRegistryApp:
    def __init__(self):
        self.registry = StudentRegistry()

    def menu(self):
        print("\nMENU")
        print("1. Add students")
        print("2. Display students")
        print("3. Statistics")
        print("4. Search student")
        print("5. Sort students")
        print("6. Update student")
        print("7. Delete student")
        print("8. Exit")

    def run(self):
        print("Student Registry System Started.")

        while True:
            self.menu()
            choice = input("Choose (1–8): ")

            if choice == '1':
                self.registry.add_students()
            elif choice == '2':
                self.registry.display()
            elif choice == '3':
                self.registry.statistics()
            elif choice == '4':
                self.registry.search()
            elif choice == '5':
                self.registry.sort_students()
            elif choice == '6':
                self.registry.update_student()
            elif choice == '7':
                self.registry.delete_student()
            elif choice == '8':
                print("Exiting program.")
                break
            else:
                print("Invalid option.")


# ---------------- ENTRY POINT ---------------- #

if __name__ == "__main__":
    app = StudentRegistryApp()
    app.run()
