def play_Riddle_it_Roulette():
    print("\033[1;32m" + "Welcome to Riddle It Roulette" + "\033[0m") 
    print("\033[1;32m" + "Let's Begin. You will be given a phrase to guess the word I have in mind." + "\033[0m")
    print("\033[1;32m" + "Get it right, you move on. Get it wrong, you lose a life!" + "\033[0m")
    print("\033[1;32m" + "Lose 3 times, it's game over." + "\033[0m")

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
                print("\033[1;32;40m" + "congrats\n" + "\033[0m")  # Green text on black background
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
                print("\033[1;31m" + "That's Not Correct {}. {} lives left.\n".format(life - attempts, attempts) + "\033[0m")  

        games += 1
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            game_running = False
            print("\nScore: {}".format(score))
            print("Games Played: {}".format(games))
            print("Average Score: {}".format(score / games))

while True:
    print("Welcome To Our App! Select The Game You Want To Play")
    print() # Colour Scheme from (Studytonight.com)
    print("\033[0;32m" + "1. Riddle It Roulette" + "\033[0m")  
    print("\033[0;34m" + "2. Game 2" + "\033[0m")  
    print("\033[1;35m" + "3. Game 3" + "\033[0m")  
    print("\033[1;31m" + "4. Game 4" + "\033[0m")  
    print()

    game = int(input("Select The Corresponding Number For The Game You Want To Play "))

    if game == 1:
        play_Riddle_it_Roulette()
    elif game == 2:
        print("Game 2")
    elif game == 3:
        print("Game 3")
    elif game == 4:
        print("Game 4")
    else:
        print("\033[1;31m" + "Invalid option" + "\033[0m")  # Red text on black background

    play_again = input("Do you want to play another game? (yes/no): ").lower()
    if play_again != "yes":
        break
