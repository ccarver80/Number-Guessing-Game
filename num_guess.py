
# Number gussing game from Chapter 3 of "Invent your own computer 
# games with Python," by Al Sweigart


import random
import time #not part of the instructions but wanted to play with this feature

num_guesses = 0

print("Hello, what is your name?")
myName = input()

rdm_number = random.randint(1,30) #made it more difficult than the book
print('Hello, ' + myName + ' I am thinking of a number between 1 - 30')

time.sleep(2) #let time for people to read the opening statment

for num_guesses in range(6):
    guess = input('\nWhat number am I thinking of?: ')
    guess = int(guess)

    if guess < 1:
        print('I said a number between 1 - 30') # not part of the book, check and count against turn
        continue

    if guess > 30:
        print('I said a number between 1 - 30') #not part of the book, check and count against turn 
        continue

    if rdm_number < guess:
        print('\nYour guess is to high! Please try again')

    if rdm_number > guess:
        print('\nYour guess is to low! Please try again')

    if rdm_number == guess:
        break

if rdm_number == guess:
    num_guesses = str(num_guesses + 1)
    print('\nGreat job ' + myName + '! You got the number in ' + num_guesses + ' guesses!')

if rdm_number != guess:
    rdm_number = str(rdm_number)
    print('\nSorry the number I was thinking was ' + rdm_number)

