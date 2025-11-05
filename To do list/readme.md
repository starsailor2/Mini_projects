# 📝 To-Do List CLI Application

A simple yet powerful command-line To-Do List application built with Python. Manage your tasks efficiently with features like add, edit, delete, and mark tasks as complete. All data is persisted in a JSON file.

## ✨ Features

- ✅ **Add Tasks** - Create new tasks with title and description
- ✏️ **Edit Tasks** - Update existing task details
- 🗑️ **Delete Tasks** - Remove tasks you no longer need
- ✔️ **Mark as Complete** - Track your progress by marking tasks as done
- 📋 **View Tasks** - Display all, pending, or completed tasks
- 💾 **Data Persistence** - All tasks saved automatically to JSON file
- 🕒 **Timestamps** - Track when tasks were created and last updated

## 🛠️ Technologies & Concepts

- **Python 3.10+** (uses match-case statements)
- **JSON** for data storage
- **Datetime module** for timestamp management
- **File I/O operations**
- **Object-oriented principles**
- **Menu-driven interface**

## 📋 Prerequisites

- Python 3.10 or higher (required for match-case syntax)

## 🚀 Installation & Setup

1. **Clone or download** this project to your local machine

2. **Navigate** to the project directory:
   ```bash
   cd "c:\Users\srish\Downloads\Mini_projects\To do list"
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## 💡 Usage

When you run the application, you'll see a menu with the following options:

```
==============================
🧭 TO-DO LIST MENU
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
```

### Adding a Task
1. Select option `1`
2. Enter task title
3. Enter task description
4. Task will be saved automatically

### Editing a Task
1. Select option `2`
2. Enter the task ID
3. Enter new title (or leave blank to keep current)
4. Enter new description (or leave blank to keep current)

### Deleting a Task
1. Select option `3`
2. Enter the task ID to delete
3. Confirm deletion

### Marking Tasks as Complete
1. Select option `4`
2. Enter the task ID
3. Task status will be updated to "Completed"

## 📁 File Structure

```
To do list/
│
├── main.py          # Main application file
├── data.json        # Auto-generated file storing tasks
└── README.md        # This file
```

## 📊 Data Structure

Tasks are stored in JSON format with the following structure:

```json
[
    {
        "id": 1,
        "title": "Example Task",
        "description": "Task description here",
        "status": "Pending",
        "created_at": "2025-11-05 10:30",
        "updated_at": "2025-11-05 10:30"
    }
]
```

## 🎯 Learning Outcomes

This project demonstrates:
- ✅ Working with Lists & Dictionaries
- ✅ Loops and Conditional Logic
- ✅ File Handling (JSON read/write)
- ✅ Datetime manipulation
- ✅ Menu-driven interface using match-case
- ✅ Error handling with try-except
- ✅ Function organization and modularity

## 🤝 Contributing

Feel free to fork this project and add your own features! Some ideas:
- Add due dates for tasks
- Priority levels (High, Medium, Low)
- Categories or tags
- Search functionality
- Export tasks to CSV

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

Created as part of a Python mini-projects collection.

---

**Happy Task Managing! 🎉**