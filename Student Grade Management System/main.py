import json
import os
import time

JSON_FILE = os.path.join(os.path.dirname(__file__), 'Student.json')
def load_students():
    if not os.path.exists(JSON_FILE) or os.stat(JSON_FILE).st_size == 0:
        print(f"File '{JSON_FILE}' not found or is empty")
        return []
    
    try:
        with open(JSON_FILE,'r') as file:
            Students = json.load(file)
            if isinstance(Students, list):
                print(f"Successfully loaded {len(Students)} student records from {JSON_FILE}.")
                return Students
            else:
                print(f"Warning: Expected a list in {JSON_FILE}, but got {type(Students).__name__}.")
                return []
            
    except json.JSONDecodeError:
        print(f"\n Warning: JSON file '{JSON_FILE}' is corrupted. Starting with an empty dictionary.")
        return []
    except Exception as e:
        print(f"\n An unexpected error occurred during file loading: {e}. Starting with an empty dictionary.")
        return []

def show_students(Students):
    roll = int(input("Enter the roll no. of the students you want to find: "))

    for student in Students:
        if student["Roll No."] == roll:
            print(student)
            return 
        
    print("Student not found")
    return None

def add_student():
    global Students
    print("Add the student Name , Roll no. and the marks of the subjects ")
    name =  input("Enter the name of the student: ")
    roll = int(input("Enter the Roll No.: "))
    subjects = ['Maths','Science','English','Social science','General knowledge']
    marks = {}

    total = 0

    for i in subjects:
        score = float(input(f"Enter the marks of {i}: "))
        marks[i] = score
        total += score
    
    avg = total/len(subjects)

    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B+"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C+"
    elif avg >= 40:
        grade = "C"
    else:
        grade = "F"

    student = {"Name":name, "Roll No.":roll, "Average":avg, "Grade":grade}
    Students.append(student)

    try:
        with open(JSON_FILE, 'w') as file:
            json.dump(Students, file, indent = 4)

            print(f"successfully saved the data to {JSON_FILE}")

    except IOError:
        print(f"Error: could not write into the file {JSON_FILE}")


    print(f"Student {name} added successfully\n")
    
def update_student():
    pass

def delete_student():
    pass

def top_student():
    pass


def menu():
    print("\n----------Welcome to our Student management system--------\n")
    print("press 1 for view the students details")   
    print("Press 2 for Add the students")
    print("press 3 for update the student details")
    print("press 4 for delete the student")
    print("press 5 for see the top n students")
    print("press 6 for see the Student dictionary")
    print("press any other key to exit")


print("Student Library is loading from json file...")
Students = load_students()

delay_time = 2
time.sleep(delay_time)


while True:
    
    menu()

    choice = input("Enter the choice: ")

    match choice:
        
        case "1":
            show_students(Students)
        
        case "2":
            add_student()

        case "3":
            update_student()

        case "4":
            delete_student()

        case "5":
            top_student()        

        case "6":
            print("print the Students dictionary")
            print(Students)

        case _:
            print("exit....")
            break
        
