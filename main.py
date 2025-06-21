# Simple To-Do List in Python
print("hello")
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed: {task}")
    else:
        print("Task not found!")

def view_tasks():
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

while True:
    print("\nOptions: add, remove, view, quit")
    choice = input("Enter command: ").lower()

    if choice == "add":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "remove":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "view":
        view_tasks()
    elif choice == "quit":
        break
    else:
        print("Invalid command!")
