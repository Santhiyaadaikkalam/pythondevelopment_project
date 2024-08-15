import random

def get_computer_choice():
    """Randomly choose Rock, Paper, or Scissors for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if ((user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")):
        return "You win!"
    
    return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        print("\nOptions: rock, paper, scissors, or exit to quit")
        user_choice = input("Enter your choice: ").lower()

        if user_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
