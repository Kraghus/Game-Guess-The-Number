
import random # import random number generation capabilities

# declare global constant
CONST_MAX_GUESSES = 7 # using a CONST for future feature

# get the player name
print('Please enter your name: ', end='')
player_name = input()
print('')

# greet the player and explain the rules of the game
print('Hello, ' + player_name + '! Let\'s play a game! I\'m thinking of a random number between 1 and 100. Try to guess what it is!')
print('')


# declare variables for the number of guesses a player has used and the integer that they guessed
bool_continue_game = True
guess_number = 0
player_guess = 0

# overall game loop. will continue looping until the player no longer wishes to continue play
while bool_continue_game == True:    

    # get the random number
    random_number = random.randint(1, 100)

    # single game loop. continues play until the maximum number of guesses has been reached
    while guess_number < CONST_MAX_GUESSES:
        try:
            # get the guess from the player
            guess_number += 1
            print('Enter guess #' + str(guess_number) + ': ', end='')
            player_guess = input()
    
            # compare the guess with the actual number, give feedback to the player, and use a guess
            if int(player_guess) > random_number:
                print('That guess was too high...')
                print('')
                continue
    
            # compare the guess with the actual number, give feedback to the player, and use a guess
            elif int(player_guess) < random_number:
                print('That guess was too low...')
                print('')
                continue
    
        # catches any invalid input and gives feedback to the player
        except:
            print('Invalid input detected, please make sure your guess is a whole number.')
            print('')
        
            # gives the player their guess back in case they wasted it on invalid input
            guess_number -= 1
    
        # this code only executes if the player guesses the correct number
        else:
            break    


    # if the player guesses the correct number, print the message for a win
    if int(player_guess) == random_number:
        if guess_number == 1:
            print('')
            print ('Congratulations, ' + player_name + '! You have correctly guessed the number ' + str(random_number) + ' in ' + str(guess_number) + ' guess and won the game!')
            print('')
        
        else:
            print('')
            print('Congratulations, ' + player_name + '! You have correctly guessed the number ' + str(random_number) + ' in ' + str(guess_number) + ' guesses and won the game!')
            print('')

    # if the player does not guess the correct number, print the message for a loss
    else:
        print('You have exceeded the maximum number of guesses and lost the game... the number was ' + str(random_number) + '! Better luck next time, ' + player_name + '!')
        print('')

    # ask the player if they would like to play again
    print('Would you like to play again, ' + player_name + '? (Y for YES, N for NO): ', end='')
    play_again = input()

    # resets the relevant counts and starts a new game
    if play_again == 'Y' or play_again == 'y': 
        guess_number = 0
        player_guess = 0
        print('')
        print('Ok! I\'m thinking of another number between 1 and 100. Try to guess what it is!')
        print('')
        continue
    
    # terminates the overall game loop, thus ending the game
    else:
        bool_continue_game = False
        print('')
        print('Ending game... catch you later, ' + player_name + '!')
        print('')
        break



    

    

    

    

    

    