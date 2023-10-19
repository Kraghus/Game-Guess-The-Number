
import random # import random number generation capabilities
import sys # used to exit the game after completion


# declare global constant
CONST_MAX_GUESSES = 7

# get the player name
print('Please enter your name: ', end='')
player_name = input()
print('')

# greet the player and explain the rules of the game
print('Hello, ' + player_name + '! Let\'s play a game! I\'m thinking of a random number between 1 and 100. Try to guess what it is!')
print('')

# get the random number
random_number = random.randint(1, 100)
print(random_number) # for testing purposes
print('')

number_of_guesses_left = CONST_MAX_GUESSES
guess_number = 0
player_guess = 0

# continues play until the maximum number of guesses has been reached
while number_of_guesses_left > 0:
    # get the guess from the player
    guess_number += 1
    print('Enter guess #' + str(guess_number) + ': ', end='')
    player_guess = input()
    
    # compare the guess with the actual number, give feedback to the player, and use up a guess
    if int(player_guess) > random_number:
        print('That guess was too high...')
        print('')
        number_of_guesses_left -= 1
        continue
    
    # compare the guess with the actual number, give feedback to the player, and use up a guess
    elif int(player_guess) < random_number:
        print('That guess was too low...')
        print('')
        number_of_guesses_left -= 1
        continue
    
    # this code only executes if the player guesses the correct number
    else:
        break    


# if the player guesses the correct number, print the message for a win
if int(player_guess) == random_number:
    if guess_number == 1:
        print ('Congratulations, ' + player_name + '! You have correctly guessed the number ' + str(random_number) + ' in ' + str(guess_number) + ' guess and won the game!')
        print('')
        sys.exit
        
    else:
        print('Congratulations, ' + player_name + '! You have correctly guessed the number ' + str(random_number) + ' in ' + str(guess_number) + ' guesses and won the game!')
        print('')
        sys.exit(0)

# if the player does not guess the correct number, print the message for a loss
else:
    print('You have exceeded the maximum number of guesses and lost the game... the number was ' + str(random_number) + '! Better luck next time, ' + player_name + '!')
    print('')
    sys.exit(0)
    

    

    

    

    

    