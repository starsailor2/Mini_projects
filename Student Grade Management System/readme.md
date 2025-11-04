# 📚 Student Grade Management System

A comprehensive command-line application to manage student records, track academic performance across multiple subjects, and generate performance analytics. Built with Python using JSON for data persistence and efficient data structures for student information management.

---

## 🚀 Features

- **Add Student Records**: Store student information with marks across 5 subjects
- **View Student Details**: Search and display individual student records by roll number
- **Update Records**: Modify student name, roll number, or marks with automatic grade recalculation
- **Delete Students**: Remove student records with confirmation prompt
- **Top Performers**: Display top N students ranked by average marks
- **Auto-Grade Calculation**: Automatic grade assignment based on average performance
- **Data Persistence**: Save and load data from JSON file automatically
- **Input Validation**: Error handling for file operations and user inputs

---

## 🧱 How It Works

### Data Structure
- Students are stored as a list of dictionaries:
  ```python
  Students = [
      {
          "Name": "John Doe",
          "Roll No.": 101,
          "Average": 85.6,
          "Grade": "A"
      },
      ...
  ]
  ```

### Subjects Tracked
The system tracks marks for 5 subjects:
- Mathematics
- Science
- English
- Social Science
- General Knowledge

### Grading Scale
```python
A+ : 90-100
A  : 80-89
B+ : 70-79
B  : 60-69
C+ : 50-59
C  : 40-49
F  : Below 40
```

---

## 📦 Requirements
- Python 3.10+ (uses `match-case` statement)
- No external libraries required
- Built-in modules: `json`, `os`, `time`

---

## 🛠️ Usage

### Installation
1. Clone or download the repository
2. Ensure you have Python 3.10 or higher installed
3. Navigate to the project directory

### Running the Application
```bash
python main.py
```

### Menu Options
```
1. View Student Details    - Search student by roll number
2. Add Student             - Add new student with marks
3. Update Student          - Modify existing student records
4. Delete Student          - Remove student from database
5. Top N Students          - View top performers
6. View All Students       - Display complete database
Any other key              - Exit the application
```

---

## 📂 File Structure
```
Student_Grade_Management_System/
├── main.py
├── Student.json       # auto-generated data file
└── README.md
```

---

## 🧪 Example Flow

### Adding a Student
```
Enter choice: 2
Add the student Name, Roll no. and the marks of the subjects
Enter the name of the student: Alice Smith
Enter the Roll No.: 101
Enter the marks of Maths: 95
Enter the marks of Science: 88
Enter the marks of English: 92
Enter the marks of Social science: 85
Enter the marks of General knowledge: 90

Student Alice Smith added successfully
Average: 90.0, Grade: A+
```

### Viewing Student Details
```
Enter choice: 1
Enter the roll no. of the students you want to find: 101

{'Name': 'Alice Smith', 'Roll No.': 101, 'Average': 90.0, 'Grade': 'A+'}
```

### Updating Student Information
```
Enter choice: 3
Enter the roll no. of the student to update: 101

Current details: {'Name': 'Alice Smith', 'Roll No.': 101, 'Average': 90.0, 'Grade': 'A+'}

What would you like to update?
1. Name
2. Roll Number
3. Marks (will recalculate average and grade)
4. Update All

Enter choice: 1
Enter new name: Alice Johnson
Student updated successfully!
```

### Top N Students
```
Enter choice: 5
How many top students do you want to see? 3

--- Top 3 Students ---
1. Alice Johnson (Roll: 101) - Average: 90.00, Grade: A+
2. Bob Williams (Roll: 102) - Average: 85.60, Grade: A
3. Charlie Brown (Roll: 103) - Average: 78.40, Grade: B+
```

---

## 🧠 Core Functions

### `load_students()`
- Loads student data from `Student.json`
- Handles missing/corrupted files gracefully
- Returns empty list if file doesn't exist

### `save_student()`
- Saves current student data to JSON file
- Formats JSON with indentation for readability
- Called automatically after add/update/delete operations

### `calculate_grade(avg)`
- Calculates letter grade based on average marks
- Uses 7-tier grading system (A+ to F)
- Returns grade string

### `add_student()`
- Prompts for student name and roll number
- Collects marks for all 5 subjects
- Calculates average and assigns grade automatically
- Saves to JSON file

### `show_students(Students)`
- Searches student by roll number
- Displays complete student record
- Returns None if student not found

### `update_student()`
- Allows selective updates (name, roll, or marks)
- Option to update all fields at once
- Recalculates average/grade when marks are updated
- Auto-saves after successful update

### `delete_student()`
- Finds student by roll number
- Asks for confirmation before deletion
- Updates JSON file after deletion

### `top_student()`
- Accepts N as input for top N students
- Sorts students by average (descending)
- Uses lambda function for sorting
- Displays ranked list with details

---

## 🎯 Key Programming Concepts

### Used in This Project
- **Data Structures**: Lists and dictionaries
- **File I/O**: JSON read/write operations
- **Functions**: Modular code organization
- **Lambda Functions**: Sorting with custom key
- **Match-Case Statement**: Menu-driven interface (Python 3.10+)
- **Error Handling**: try-except for file operations
- **Global Variables**: Shared student data
- **String Formatting**: f-strings for output
- **Control Flow**: while loops, for loops, conditionals

---

## ⚠️ Error Handling

The system handles:
- **Missing JSON file**: Creates new empty list
- **Corrupted JSON**: Starts with empty database
- **File write errors**: Displays error message
- **Invalid user inputs**: Prompts for re-entry
- **Student not found**: Clear feedback message

---

## 💡 Tips for Users

1. **Roll Numbers**: Ensure roll numbers are unique
2. **Marks Range**: Enter marks between 0-100 for accurate grading
3. **Backup**: Regularly backup `Student.json` file
4. **Updates**: When updating marks, all 5 subjects must be re-entered
5. **Deletion**: Deleted records cannot be recovered

---

## 🐛 Known Issues

- Duplicate roll numbers are not prevented
- Subject marks are not stored individually in JSON
- No undo functionality for deletions
- Limited to 5 predefined subjects

---

## 👨‍💻 Author
Built by **Rishav** — passionate about practical AI/ML projects and productivity tools!

---

## 📝 License
This project is open source and available for educational purposes.

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

---

## 📧 Contact
For questions or suggestions, feel free to reach out!

---

**Happy Learning! 📚✨**