import random

def get_user_choice():
    """
    Get the user's choice (Rock, Paper, or Scissors).
    """
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """
    Get the computer's choice (Rock, Paper, or Scissors).
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of the game based on the choices made.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """
    Play a round of Rock, Paper, Scissors.
    """
    print("Let's play Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

def play_again():
    """
    Check if the player wants to play again.
    """
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again in ["y", "n"]:
            return play_again == "y"
        else:
            print("Invalid choice. Please try again.")

def main():
    """
    Main entry point of the program.
    """
    while True:
        play_game()
        if not play_again():
            break

if __name__ == "__main__":
    main()
