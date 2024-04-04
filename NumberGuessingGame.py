import random

def number_guessing_game():
    print("Welcome to The Number Hunter!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")
    print("For each correct guess, you earn 10 points.")

    min_num = 1
    max_num = 100
    max_attempts = 10
    total_points = 0
    rounds_played = 0

    while True:
        rounds_played += 1
        points = 0

        secret_number = random.randint(min_num, max_num)
        attempts = 0

        print(f"\nRound {rounds_played}:")
        print(f"I'm thinking of a number between {min_num} and {max_num}. You have {max_attempts} attempts.")

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < min_num or guess > max_num:
                    print(f"Please guess within the range {min_num} and {max_num}.")
                elif guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                    points += 10
                    print(f"You earned {points} points.")
                    total_points += points
                    break
            except ValueError:
                print("Please enter a valid number.")

        if attempts >= max_attempts:
            print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            print(f"Total rounds played: {rounds_played}")
            print(f"Total points earned: {total_points}")
            break

if __name__ == "__main__":
    number_guessing_game()