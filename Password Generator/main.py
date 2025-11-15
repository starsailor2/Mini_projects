"""
Simple Password Generator
Generating passwords with atleast 8 characters which includes:
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 digit
- At least 1 symbol
"""

import secrets 
import string

def generate_simple_password(length=15):
    # Validate length
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")
    
    # Define character sets
    lowercase = string.ascii_lowercase  # a-z
    uppercase = string.ascii_uppercase  # A-Z
    digits = string.digits              # 0-9
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"  # Common symbols
    
    # Ensure at least one character from each category
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    
    # Fill the rest with random characters from all sets
    all_chars = lowercase + uppercase + digits + symbols
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_chars))
    
    # Shuffle to remove predictable ordering
    secrets.SystemRandom().shuffle(password_chars)
    
    return ''.join(password_chars)


def main():
    """Main function with user interaction and error handling."""
    print("=" * 50)
    print("Simple Secure Password Generator")
    print("=" * 50)
    print("\nRequirements:")
    print("- Minimum 8 characters")
    print("- At least 1 uppercase letter")
    print("- At least 1 lowercase letter")
    print("- At least 1 digit")
    print("- At least 1 symbol")
    print()
    
    while True:
        try:
            # Get user input
            length_input = input("Enter password length (minimum 8, press Enter for 12): ").strip()
            
            # Use default if empty
            if length_input == "":
                length = 15
            else:
                length = int(length_input)
            
            # Generate password
            password = generate_simple_password(length)
            
            # Display result
            print("\n" + "=" * 50)
            print(f"Generated Password: {password}")
            print(f"Length: {len(password)} characters")
            print("=" * 50)
            print("\n Important: Store this password in a password manager!")
            print()
            
            # Ask to generate another
            again = input("Generate another password? (y/n): ").strip().lower()
            if again != 'y':
                print("\nThank you for using Simple Password Generator!")
                break
            print()
            
        # Handle errors
        except ValueError as e:
            print(f"\n Error: {e}")
            print("Please try again.\n")
        except KeyboardInterrupt:
            print("\n\nExiting... Goodbye!")
            break
        except Exception as e:
            print(f"\n Unexpected error: {e}")
            print("Please try again.\n")


if __name__ == '__main__':
    main()