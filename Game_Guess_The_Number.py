
import random # import random number generation capabilities

# declare global constant for max number of guesses
CONST_MAX_GUESSES = 7

# get the player name
print("Please enter your name: ", end="")
player_name = input()

# greet the player and explain the rules of the game
print("\nHello, " + player_name + "! Let's play a game! I'm thinking of a random number between 1 and 100. Try to guess what it is!\n")

# declare variables for the application loop, number of guesses a player has used, and the integer that they guessed
bool_continue_game = True
guess_number = 0
player_guess = 0

# application loop. loops until the player no longer wishes to continue
while bool_continue_game == True:    

    # get the random number
    random_number = random.randint(1, 100)
    print(random_number)

    # single game loop. continue play until the maximum number of guesses has been reached
    while guess_number < CONST_MAX_GUESSES:
        try:
            # get the guess from the player
            guess_number += 1
            print("Enter guess #" + str(guess_number) + ": ", end="")
            player_guess = input()
    
            # compare the guess with the actual number, give feedback to the player, and use a guess
            if int(player_guess) > random_number:
                print("That guess was too high...\n")
                continue
    
            # compare the guess with the actual number, give feedback to the player, and use a guess
            elif int(player_guess) < random_number:
                print("That guess was too low...\n")
                continue
    
        # catch any invalid input and give feedback to the player
        except:
            print("Invalid input detected, please make sure your guess is a whole number.\n")
        
            # give the player their guess back in case they wasted it on invalid input
            guess_number -= 1
    
        # execute if the player guesses the correct number to end the game
        else:
            break    

    # if the player guessed the correct number, print the message for a win
    if int(player_guess) == random_number:
        if guess_number == 1:
            print ("\nCongratulations, " + player_name + "! You have correctly guessed the number " + str(random_number) + " in " + str(guess_number) + " guess and won the game!\n")
        
        else:
            print("\nCongratulations, " + player_name + "! You have correctly guessed the number " + str(random_number) + " in " + str(guess_number) + " guesses and won the game!\n")

    # if the player did not guess the correct number, print the message for a loss
    else:
        print("You have exceeded the maximum number of guesses and lost the game... the number was " + str(random_number) + "! Better luck next time, " + player_name + "!\n")

    # ask the player if they would like to play again
    print("Would you like to play again, " + player_name + "? (Y for YES, N for NO): ", end="")
    play_again = input()
    
    while play_again != 'Y' or play_again != 'Y' or play_again != 'N' or play_again != 'n':

        # reset the relevant counts and start a new game
        if play_again == 'Y' or play_again == 'y': 
            guess_number = 0
            player_guess = 0
            print("\nOk! I'm thinking of another number between 1 and 100. Try to guess what it is!\n")
            break
    
        # terminate the overall game loop, thus ending the game
        elif play_again == 'N' or play_again == 'n':
            bool_continue_game = False
            print("\nEnding game... catch you later, " + player_name + "!\n")
            break
        
        # execute repeatedly for invalid input
        else:
            print("\nInvalid input detected. Would you like to play again, " + player_name + "? (Y for YES, N for NO): ", end="")
            play_again = input()
            continue
        



    

    

    

    

    

    