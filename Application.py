def play_Riddle_it_Roulette():
    print()
    print("\033[1;32m" + "Welcome to Riddle It Roulette" + "\033[0m") 
    print("\033[1;32m" + "Let's Begin. You will be given a phrase to guess the word I have in mind." + "\033[0m")
    print("\033[1;32m" + "Get it right, you move on. Get it wrong, you lose a life!" + "\033[0m")
    print("\033[1;32m" + "Lose 3 times, it's game over." + "\033[0m")
    print()
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
            print("\033[1;32m" + "Hint: " + hint + "\033[0m")  

            if word_display.lower() == word_to_guess:
                print("\n\033[1;33m" + "Thats Correct! {} Was The Word".format(word_to_guess) + "\033[0m") 
                score += 1
                print("\033[1;32;40m" + "congrats\n" + "\033[0m")  
                break

            if attempts >= life:
                print("\n\033[1;31m" + "You Ran Out of Lives!, The Word Was {}\n".format(word_to_guess) + "\033[0m")  
                break

            guess = input("Enter The Correct Word To Proceed: ").lower()

            if guess == word_to_guess:
                print("\n\033[1;33m" + "Thats Correct! {} Was The Word".format(word_to_guess) + "\033[0m")  
                score += 1
                print("\033[1;32m" + "congrats\n" + "\033[0m")  
                break
            else:
                attempts += 1
                print("\033[1;31m" + "That's Not Correct {} lives left.\n".format(life - attempts, attempts) + "\033[0m")  

        games += 1
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            game_running = False
            print("\nScore: {}".format(score))
            print("Games Played: {}".format(games))
            print("Average Score: {}".format(score / games))
            
def play_number_guessing_game():
    print()
    print("\033[0;34m" + "Welcome to The Number Hunter!" + "\033[0m")
    print("\033[0;34m" + "I'm thinking of a number between 1 and 100." + "\033[0m")
    print("\033[0;34m" + "You have 10 attempts to guess the number." + "\033[0m")
    print("\033[0;34m" + "For each correct guess, you earn 10 points." + "\033[0m")
    print()
    import random

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
        print("\033[0;34m" + f"I'm thinking of a number between {min_num} and {max_num}. You have {max_attempts} attempts." + "\033[0m")

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < min_num or guess > max_num:
                    print(f"Please guess within the range {min_num} and {max_num}.")
                elif guess < secret_number:
                    print()
                    print("Too low! Try again.")
                    print()
                elif guess > secret_number:
                    print("Too high! Try again.")
                    print()
                else:
                    print()
                    print("\033[0;33m" + f"Congratulations! You guessed the number {secret_number} in {attempts} attempts." + "\033[0m")
                    points += 10
                    print("\033[0;34m" + f"You earned {points} points." + "\033[0m")
                    print()
                    total_points += points
                    break
            except ValueError:
                print("Please enter a valid number.")
                print()

        if attempts >= max_attempts:
            print("\033[0;31m" + f"Sorry, you've run out of attempts. The correct number was {secret_number}." + "\033[0m")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            print(f"Total rounds played: {rounds_played}")
            print(f"Total points earned: {total_points}")
            print()
            break


def RockPaperScissorsGame():
    print()
    print("\033[3;35m" + "Welcome To Rock, Paper, Scissors" + "\033[0m")
    print("\033[3;35m" + "The Rules are Quite Simple Just Enter: rock, paper or scissors" + "\033[0m")
    print()
    import random
    
    choices = ["rock", "paper", "scissors"]
    player_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        player_input = input("\033[0;35m" + "Choose rock, paper, or scissors (or 'exit' to quit): " + "\033[0m").lower()
        if player_input == 'exit':
            break

        computer_choice = random.choice(choices)
        if player_input == computer_choice:
            draws += 1
            print("\033[0;33m" + f"Computer chose {computer_choice}. It's a draw!" "\033[0m")
            print()
        elif (player_input == "rock" and computer_choice == "scissors") or \
             (player_input == "paper" and computer_choice == "rock") or \
             (player_input == "scissors" and computer_choice == "paper"):
            player_wins += 1
            print("\033[0;32m" + f"Computer chose {computer_choice}. You win!" + "\033[0m")
            print()
        elif player_input not in ["rock", "paper", "scissors"]:
                print("Invalid Input! Please Enter: rock, paper or scissors")
                print()
                continue
        else:
            computer_wins += 1
            print("\033[0;31m" + f"Computer chose {computer_choice}. Computer wins!" + "\033[0m")
            print()
            

    total_games = player_wins + computer_wins + draws
    print("\nGame Statistics:")
    print(f"Total games: {total_games}")
    print(f"Wins: {player_wins}")
    print(f"Losses: {computer_wins}")
    print(f"Draws: {draws}")
    
def DiceBattle():
    print()
    print("\033[0;33m" + "Welcome to Dice Battle!" + "\033[0m")
    print("\033[0;33m" + "------RULES------" + "\033[0m")
    print("\033[0;33m" + "(1)Two Players take turns rolling a six standing die." + "\033[0m")
    print("\033[0;33m" + "(2)If one roll is lower than the other, the player will lose some hit points." + "\033[0m")
    print("\033[0;33m" + "(3)If both rolls have the same number, they will have a chance to heal." + "\033[0m")
    print("\033[0;33m" + "(4)The game continues until one of the players reaches 0 hit points or below, and that player loses." + "\033[0m")
    print()
    import random
    
    def Player(name, hp):
        return {'name': name, 'hp': hp}
        
    def roll_dice():
        return random.randint(1, 6)
    
    player1 = Player(input("Enter Player 1's name:  "), 20)
    player2 = Player(input("Enter Player 2's name:  "), 20)
    
    players = [player1, player2]
    current_player_index = 0
    
    while True:
        current_player = players[current_player_index]
        opponent = players[(current_player_index + 1) % 2]
        print(f"\n{current_player['name']}'s turn.")
        input("Press Enter to roll the dice...")
        
        roll1 = roll_dice()
        roll2 = roll_dice()
        print()
        print("\033[0;34m" + f"{current_player['name']} rolled: {roll1}" + "\033[0m")
        print("\033[0;36m" + f"{opponent['name']} rolled: {roll2}" + "\033[0m")
        print()
        
        if roll1 < roll2:
            hp_loss = roll2 - roll1
            print("\033[0;31m" + f"{current_player['name']} loses {hp_loss} HP." + "\033[0m")
            print()
            current_player['hp'] -= hp_loss
            
        elif roll1 > roll2:
            print("\033[0;32m" + f"{current_player['name']} wins this round. No HP lost" + "\033[0m")
            
        else:
            print("\033[0;33m" + "It's a Tie! Both players have the opportunity to heal" + "\033[0m")
            current_player['hp'] += 1
            opponent['hp'] += 1
            print("\033[0;32m" + f"{current_player['name']} and {opponent['name']} gained 1 HP" + "\033[0m")
            
        print("\033[0;34m" + f"{current_player['name']}'s HP: {current_player['hp']}" + "\033[0m")
        print("\033[0;36m" + f"{opponent['name']}'s HP: {opponent['hp']}" + "\033[0m")
        
        if current_player['hp'] <= 0:
            print("\033[0;31m" + f"{current_player['name']} has lost!" + "\033[0m")
            break
        
        current_player_index = (current_player_index + 1) % 2

while True:
    print("Welcome To Our App! Select The Game You Want To Play")
    print() # Colour Scheme from (https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python)
    print("\033[3;32m" + "1. Riddle It Roulette" + "\033[0m")  
    print("\033[3;34m" + "2. Number Guessing Game" + "\033[0m")  
    print("\033[3;35m" + "3. Rock Paper Scissor's Game" + "\033[0m")  
    print("\033[3;33m" + "4. Dice Battle" + "\033[0m")  
    print()

    game = int(input("Select The Corresponding Number For The Game You Want To Play "))

    if game == 1:
        play_Riddle_it_Roulette()
    elif game == 2:
        play_number_guessing_game()
    elif game == 3:
        RockPaperScissorsGame()
    elif game == 4:
        DiceBattle()
    else:
        print("\033[1;31m" + "Invalid option" + "\033[0m")  

    play_again = input("Do you want to play another game? (yes/no): ").lower()
    if play_again != "yes":
        break
