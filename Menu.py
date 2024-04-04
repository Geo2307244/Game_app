def play_Riddle_it_Roulette():
    print("Welcome to Riddle It Roulette")
    print("Let's Begin. You will be given a phrase to guess the word I have in mind.")
    print("Get it right, you move on. Get it wrong, you lose a life!")
    print("Lose 3 times, it's game over.\n")

    import random

    words = {
        'banana': 'A Yellow Crescent',
        'nothing': 'The Poor Have It, The Rich Need It, Eat It You Die, What is It?',
        'bank': 'It Has Branches But No Fruit, Trunk or Leaves.',
        'alphabet': 'It Contains All 26 Letters',
        'swims': 'It Can Be Read The Same Upside-Down and Right Side Up',
        'orange': 'Its a Colour You Can Eat',
        'what': 'W-H-A-T Spells what?',
        'coin': 'What Has a Head And a Tail, But No Arms or Legs?',
        'book': 'Has Many Words But Never Speaks',
        'n': 'Throw me out the window, You will have a Grieving Wife, But Drop Me In The Middle Of a Door, And You Might Just Save a Life. What Am I?',
        'stars': 'They come at night without being called and are lost in the day without being stolen. What are they?',
        'lightning': 'I touch the earth and I touch the sky, but if I touch you, you’ll likely die. What am I?',
        'three': 'If there are five apples and you take away three, how many apples do you have?',
        'bubble': ' I am lighter than air, but a hundred people cannot lift me—I’m too fragile. What am I?',
        'corn': 'You throw away the outside and cook the inside. Then you eat the outside and throw away the inside. What did you eat?',
        'eye': 'Pronounced as one letter and written with three, two letters there are and two only in me. I’m double. I’m single. I’m black, blue, and gray. I’m read from both ends, but the same either way. What am I?',
        'crows': 'You’ll often find us on a line. When we’re together, it’s a crime. What are we?',
    }

    def choose_word():
        return random.choice(list(words.items()))

    def display_word(word_to_guess, guessed_word):
        displayed_word = ''
        for letter in word_to_guess:
            if letter.lower() in guessed_word:
                displayed_word += letter
            else:
                displayed_word += '_'
        return displayed_word

    game_running = True
    score = 0
    games = 0

    while game_running:
        word_to_guess, hint = choose_word()
        guessed_word = ''
        attempts = 0
        life = 3

        while True:
            word_display = display_word(word_to_guess, guessed_word)
            print("\n" + word_display)
            print("Hint: ", hint)

            if word_display.lower() == word_to_guess:
                print("\nThats Correct! {} Was The Word".format(word_to_guess))
                score += 1
                print("congrats\n")
                break

            if attempts >= life:
                print("\nYou Ran Out of Lives!, The Word Was {}\n".format(word_to_guess))
                break

            guess = input("Enter The Correct Word To Proceed: ").lower()

            if guess == word_to_guess:
                print("\nThats Correct! {} Was The Word".format(word_to_guess))
                score += 1
                print("congrats\n")
                break
            else:
                attempts += 1
                print("That's Not Correct", life - attempts, "lives left.\n")

        games += 1
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            game_running = False
            print("\nScore: {}".format(score))
            print("Games Played: {}".format(games))
            print("Average Score: {}".format(score / games))

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


# Main code
print("Welcome To Our App! Select The Game You Want To Play")
print()
print("1. Riddle It Roulette")
print("2. The Number Hunter")
print("3. Game 3")
print("4. Game 4")
print()

game = int(input("Select The Corresponding Number For The Game You Want To Play "))

if game == 1:
    play_Riddle_it_Roulette()
elif game == 2:
    number_guessing_game()
elif game == 3:
    print("Game 3")
elif game == 4:
    print("Game 4")
else:
    print("Invalid option")

import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.reset()

    def play(self, player_choice):
        player_choice = player_choice.lower()
        computer_choice = random.choice(self.choices)
        if player_choice == computer_choice:
            self.draws += 1
            return f"Computer chose {computer_choice}. It's a draw!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            self.player_wins += 1
            return f"Computer chose {computer_choice}. You win!"
        else:
            self.computer_wins += 1
            return f"Computer chose {computer_choice}. Computer wins!"

    def reset(self):
        self.player_wins = 0
        self.computer_wins = 0
        self.draws = 0

    def game_stats(self):
        total_games = self.player_wins + self.computer_wins + self.draws
        return (f"Total games: {total_games}\n"
                f"Wins: {self.player_wins}\n"
                f"Losses: {self.computer_wins}\n"
                f"Draws: {self.draws}")

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


