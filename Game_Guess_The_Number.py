
import random # import random number generation capabilities
import sys # used to exit the game after completion


# declare variables
player_guess = 0
guess_number = 0
number_of_guesses_left = 7
random_number = 0

# get the player name
print('Please enter your name: ', end='')
player_name = input()
print('')

# greet the player and explain the rules of the game
print('Hello, ' + player_name + '! Let\'s play a game! I\'m thinking of a random number between 1 and 100. Try to guess what it is!')
print('')

# get the random number
random_number = random.randint(1, 100)
# print(random_number)

# continues play until the maximum number of guesses has been reached
while number_of_guesses_left > 0:
    # get the guess from the player
    guess_number += 1
    print('Enter guess #' + str(guess_number) + ': ', end='')
    player_guess = input()
    
    # compare the guess against the random number
    if int(player_guess) == random_number:
        print('Congratulations! You have guessed the number correctly and won the game!')
        print('')
        sys.exit(0)

    elif int(player_guess) > random_number:
        print('That guess was too high...')
        print('')
        number_of_guesses_left -= 1
        continue
    
    elif int(player_guess) < random_number:
        print('That guess was too low...')
        print('')
        number_of_guesses_left -= 1
        continue
    
print('You have exceeded the maximum number of guesses and lost the game... better luck next time!')
print('')
sys.exit(0)
    

    

    

    

    

    