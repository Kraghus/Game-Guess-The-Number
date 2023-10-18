
# import random number generation capabilities
import random

# get the player name
print('Please enter your name: ', end='')
player_name = input()

print('Hello, ' + player_name + '! Let\'s play a game! I\'m thinking of a random number between 1 and 100. Try to guess what it is!')


random_number = random.randint(1, 100)
# print(random_number)