import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def generate_id(tasks):
    if not tasks:
        return 1
    else:
        return max(task["id"] for task in tasks) + 1


def add_task(tasks):
    title = input("Enter task title: ").strip()
    description = input("Enter description: ").strip()

    new_task = {
        "id": generate_id(tasks),
        "title": title,
        "description": description,
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"\nTask '{title}' added successfully!\n")


def edit_task(tasks):
    try:
        task_id = int(input("Enter task ID to edit: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")
        return

    for task in tasks:
        if task["id"] == task_id:
            print(f"Current Title: {task['title']}")
            print(f"Current Description: {task['description']}")
            new_title = input("Enter new title (leave blank to keep same): ").strip()
            new_desc = input("Enter new description (leave blank to keep same): ").strip()

            if new_title:
                task["title"] = new_title
            if new_desc:
                task["description"] = new_desc

            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            save_tasks(tasks)
            print("Task updated successfully!\n")
            return

    print("Task not found!\n")


def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task '{task['title']}' deleted successfully!\n")
            return

    print("Task not found!\n")


def mark_complete(tasks):
    try:
        task_id = int(input("Enter task ID to mark as completed: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "Completed":
                print("Task already marked as completed!\n")
                return
            task["status"] = "Completed"
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            save_tasks(tasks)
            print(f"Task '{task['title']}' marked as completed!\n")
            return

    print("Task not found!\n")


def show_tasks(tasks, filter_by=None):
    if not tasks:
        print("No tasks available!\n")
        return


    #design the table layout
    print("\n" + "=" * 60)
    print("TO-DO LIST")
    print("=" * 60)

    # good spacing for columns using fstrings
    print(f"{'ID':<4} {'Title':<25} {'Status':<10} {'Created At':<16}")
    print("-" * 60)

    for task in tasks:
        if filter_by is None or task["status"] == filter_by:
            print(f"{task['id']:<4} {task['title'][:25]:<25} {task['status']:<10} {task['created_at']:<16}")

    print("=" * 60 + "\n")

def main():
    tasks = load_tasks()

    while True:
        print("""
                ==============================
                       TO-DO LIST MENU
                ==============================
                1. Add Task
                2. Edit Task
                3. Delete Task
                4. Mark as Completed
                5. Show All Tasks
                6. Show Pending Tasks
                7. Show Completed Tasks
                8. Exit
                ==============================
                """)

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                add_task(tasks)
            case "2":
                edit_task(tasks)
            case "3":
                delete_task(tasks)
            case "4":
                mark_complete(tasks)
            case "5":
                show_tasks(tasks)
            case "6":
                show_tasks(tasks, "Pending")
            case "7":
                show_tasks(tasks, "Completed")
            case "8":
                print("Exiting... Sayonara!!!")
                break
            case _:
                print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
