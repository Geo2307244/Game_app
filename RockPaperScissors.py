import random  # Import the random module for generating random choices.

# Define the RockPaperScissorsGame class.
class RockPaperScissorsGame:
    # Objects, classes, and methods: Define a class for the Rock Paper Scissors game.
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]  # List and concatenations: Store the possible choices in a list.
        self.reset()  # Call the reset method to initialize the game.

    # Define the play method, which takes the player's choice as input.
    def play(self, player_choice):
        player_choice = player_choice.lower()  # Strings: Convert the player's choice to lowercase for case-insensitive comparison.
        computer_choice = random.choice(self.choices)  # Random numbers: Randomly select the computer's choice.
        if player_choice == computer_choice:
            self.draws += 1  # Update the count of draws.
            return f"Computer chose {computer_choice}. It's a draw!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            self.player_wins += 1  # Update the count of player wins.
            return f"Computer chose {computer_choice}. You win!"
        else:
            self.computer_wins += 1  # Update the count of computer wins.
            return f"Computer chose {computer_choice}. Computer wins!"

    # Define the reset method to start a new game.
    def reset(self):
        self.player_wins = 0  # Reset the count of player wins.
        self.computer_wins = 0  # Reset the count of computer wins.
        self.draws = 0  # Reset the count of draws.

    # Define the game_stats method to display statistics about the game.
    def game_stats(self):
        # Descriptive analytics: Calculate and display statistics about the game.
        total_games = self.player_wins + self.computer_wins + self.draws
        return (f"Total games: {total_games}\n"
                f"Wins: {self.player_wins}\n"
                f"Losses: {self.computer_wins}\n"
                f"Draws: {self.draws}")

# Example usage:
if __name__ == "__main__":
    game = RockPaperScissorsGame()
    while True:
        player_input = input("Choose rock, paper, or scissors (or 'exit' to quit): ")
        if player_input.lower() == 'exit':
            break
        result = game.play(player_input)
        print(result)
    print("\nGame Statistics:")
    print(game.game_stats())
