import json
import hashlib
import os

USER_FILE =  os.path.join(os.path.dirname(__file__), 'users.json')

''' encode() converts the string into bytes
    hexdigest() returns a readable hash string
'''
def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_user():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_user(users):
    with open(USER_FILE,"w") as file:
        json.dump(users, file, indent = 4)            

def singup():
    users = load_user()

    username = input("Enter your Username: ")
    email = input("Your EMAIL: ")
    password = input("Your Password: ")
    secure_ques = input("Please write your security question (incase of reseting/updating the password): ")
    secure_ans = input("Please write your answer here(make it tricky): ")

    # check for user if it exists

    for u in users:
        if u["username"] == username or u["email"] == email:
            print("User already exists , please Login!")
            return
        
    users.append({
        "username":username,
        "email":email,
        "password":hash_pass(password), #save the hashed password
        "secure_ques":secure_ques,
        "secure_ans":hash_pass(secure_ans.lower()) # save the security answer
        })

    save_user(users)
    print("SignUp Successful")


def login():

    users = load_user()

    username = input("Please Enter your username: ")
    password = input("Please Enter your password: ")

    for u in users:
        if u["username"] == username or u["password"] == hash_pass(password):
            print(f"Welcome Back, {username}")
            return True
        
    print("Invalid credentials, Please Sign up")
    return False

def reset_pass():
    users = load_user()

    username = input("Enter your username: ")

    for u in users:
        if u["username"] == username:
            print(f"Please give the answer for following question\n")
            print("-" * 30)
            print(u["secure_ques"])
            ans = input("Please input answer: ")

            if hash_pass(ans.lower()) == u["secure_ans"]:
                print("You have been verified!!!")
                new_pass = input("Enter your new password: ")

                u["password"] = hash_pass(new_pass) # update the new hashed password
                save_user(users)

                print("Password reset successfully!!!")
                return
            
            else:
                print("The answer is wrong, cannot reset password.")
                return

    print("Username not found")

    
def menu():

    while True:
        print("=" * 30)

        print("What do you wanna do ?")
        print("1 for signup")
        print("2 for login")
        print("3 for reset your password")
        print("4 for Exit")

        print("=" * 30)
        
        a = input("Enter your choice:- ")

        match a:
            case "1":
                singup()

            case "2":
                login()

            case "3":
                reset_pass()

            case "4":
                print("Goodbye!!!")
                break

            case _:
                print("Please try again")

if __name__ == "__main__":
    menu()