#Guess the Number Challenge

import random

print ('Welcome to Guess the Number')
print ('Enter your Name: ')
userName = input()
mysteryNumber = random.randint(1,10)

for guessesTaken in range(1,3):
    print('Take a Guess')
    guess = int(input())

    if guess < mysteryNumber:
        print('The number is low')
    if guess > mysteryNumber:
        print('The number is high')
    else:
        break

if guess == mysteryNumber:
    print('Congratulations! It only took you ' + str(int(guessesTaken)) + ' guesses')
else:
    print('Better luck next time!')
    
