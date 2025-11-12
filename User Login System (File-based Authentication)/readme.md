# User Login System (File-based Authentication)

A simple command-line user authentication system built with Python that demonstrates secure password handling using SHA-256 hashing, masked password input, and JSON file storage.

## Features

- **User Registration (Sign Up)**: Create new user accounts with username, email, and password
- **User Login**: Authenticate existing users
- **Password Reset**: Reset forgotten passwords using security questions
- **Secure Password Storage**: Passwords are hashed using SHA-256 algorithm
- **Masked Password Input**: Passwords are displayed as asterisks (*) during input using `pwinput`
- **File-based Storage**: User data is stored in JSON format
- **Security Questions**: Custom security questions for password recovery
- **Duplicate User Prevention**: Prevents registration with existing username and email combinations

## Requirements

- Python 3.10 or higher (uses `match-case` syntax)
- Required modules:
  - `json` (standard library)
  - `hashlib` (standard library)
  - `os` (standard library)
  - `pwinput` (third-party - install separately)

## Installation

1. Clone or download this project to your local machine
2. Navigate to the project directory:
   ```bash
   cd "User Login System (File-based Authentication)"
   ```
3. Install the required third-party package:
   ```bash
   pip install pwinput
   ```

## Usage

Run the program:
```bash
python main.py
```

### Menu Options

1. **Sign Up (Option 1)**: Create a new account
   - Enter username
   - Enter email (checks for duplicate registration)
   - Enter password (masked with `*`)
   - Create a security question
   - Provide security answer (masked with `*`)

2. **Login (Option 2)**: Access your account
   - Enter username
   - Enter password (masked with `*`)
   - System verifies credentials against stored hashed passwords

3. **Reset Password (Option 3)**: Recover your account
   - Enter username
   - Answer your security question (masked with `*`)
   - Set a new password (masked with `*`)

4. **Exit (Option 4)**: Close the application

## File Structure

```
User Login System (File-based Authentication)/
│
├── main.py          # Main application file
├── users.json       # User data storage (auto-generated)
└── README.md        # This file
```

## Security Features

- **SHA-256 Password Hashing**: All passwords are hashed using SHA-256 before storage
- **Security Answer Hashing**: Security question answers are also hashed for protection
- **Case-insensitive Answers**: Security answers are converted to lowercase for consistency
- **Masked Input**: Uses `pwinput` library to mask password and security answer input with asterisks
- **No Plain Text Storage**: Passwords and security answers are never stored in plain text

## Code Structure

### Key Functions

- **`hash_pass(password)`**: Hashes passwords using SHA-256
- **`load_user()`**: Loads user data from JSON file
- **`save_user(users)`**: Saves user data to JSON file
- **`singup()`**: Handles user registration with duplicate checking
- **`login()`**: Authenticates users with hashed password verification
- **`reset_pass()`**: Allows password reset using security questions
- **`menu()`**: Main menu loop using match-case syntax

<!-- ## Future Enhancements

- Add password strength validation (minimum length, special characters)
- Implement email format validation
- Add salt to password hashing for enhanced security
- Add database support (SQLite/PostgreSQL)
- Implement session management and timeout
- Add input validation and sanitization
- Add logging functionality for security auditing
- Implement account lockout after failed attempts
- Add "Remember Me" functionality
- Support for multiple security questions
- Email-based password reset option -->

## Example Workflow

```
=========================
What do you wanna do ?
1 for signup
2 for login
3 for reset your password
4 for Exit
=========================
Enter your choice:- 1

Please Enter your credential for SIGNUP
Enter your Username: john_doe
Your EMAIL: john@example.com
Your Password: ********
Please write your security question (incase of reseting/updating the password): What is your pet's name?
Please write your answer here(make it tricky): ******

SignUp Successful
```

## Troubleshooting

### Import Error: No module named 'pwinput'
```bash
pip install pwinput
```

### FileNotFoundError
The program automatically creates `users.json` if it doesn't exist. Ensure you have write permissions in the directory.

### Password Not Matching
- Ensure you're entering the exact password (case-sensitive)
- Security answers are converted to lowercase automatically

## Dependencies

- **pwinput**: Cross-platform password input with masking support
  - GitHub: https://github.com/asweigart/pwinput
  - Works on Windows, macOS, and Linux

## License

This project is for educational purposes.

## Author

Created as a mini-project for learning Python authentication concepts and secure coding practices.

