import random

def get_valid_input(value, min_val=None, max_val=None):
    """Get and validate user input"""
    while True:
        try:
            value = int(input(value))
            if min_val is not None and value < min_val:
                print(f"Please enter a number >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a number <= {max_val}")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def select_difficulty():
    """Let player choose difficulty level"""
    print("\n=== Select Difficulty ===")
    print("1. Easy (1-50, 15 attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 7 attempts)")
    
    choice = get_valid_input("Choose difficulty (1-3): ", 1, 3)
    
    difficulties = {
        1: (50, 15),
        2: (100, 10),
        3: (200, 7)
    }
    return difficulties[choice]

def play_game():
    """Main game logic"""
    upper_bound, max_attempts = select_difficulty()
    lower_bound = 1
    
    print(f"\nGuess the number between {lower_bound} and {upper_bound}")
    print(f"You have {max_attempts} attempts!\n")
    
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        guess = get_valid_input(
            f"Attempt {attempts}/{max_attempts} - Enter your guess: ",
            lower_bound,
            upper_bound
        )
        
        if guess == target_number:
            print(f"\nCongratulations! You guessed it in {attempts} attempt(s)!")
            return attempts  # Return score for tracking
        elif guess > target_number:
            print(f"Too high! {remaining - 1} attempts remaining.")
        else:
            print(f"Too low! {remaining - 1} attempts remaining.")
    
    print(f"\nGame Over! The number was {target_number}")
    return None  # No score if failed

def main():
    """Main program loop"""
    print("=" * 50)
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print("=" * 50)
    
    best_score = None
    games_played = 0
    
    while True:
        score = play_game()
        games_played += 1
        
        if score and (best_score is None or score < best_score):
            best_score = score
            print(f"New best score: {best_score} attempts!")
        
        if best_score:
            print(f"\nStats: Games played: {games_played} | Best score: {best_score}")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()