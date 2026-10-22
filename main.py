
print("================================")
print("   PYTHON STUDENT TASK MANAGER")
print("================================")

tasks = []

while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
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
