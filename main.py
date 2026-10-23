
import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()

print("================================")
print("   PYTHON STUDENT TASK MANAGER")
print("================================")

while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks added yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
