"""
Simple To-Do List Application
Run with: python todo_app.py
"""

import json
import os

DATA_FILE = "todos.json"


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!\n")
        return
    print("\n--- YOUR TO-DO LIST ---")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")
    print()


def add_task(tasks):
    title = input("Enter a new task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"Added: '{title}'")
    else:
        print("Task cannot be empty.")


def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"Marked '{tasks[num - 1]['title']}' as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: '{removed['title']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()
    menu = """
======= TO-DO LIST APP =======
1. View tasks
2. Add task
3. Mark task complete
4. Delete task
5. Exit
===============================
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
