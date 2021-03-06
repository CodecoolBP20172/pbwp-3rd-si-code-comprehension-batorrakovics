import random
#Imports the random module which is generates random things, in our case, a number.
guessesTaken = 0
#This is a variable which will be used to count how many guesses the user have used.
print('Hello! What is your name?')
myName = input()
#It prints a greeting and asks the user for his or her name
number = random.randint(1, 20)
#This is a variable containing a number in our case generated by the random module between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
#The program states that it has a number and calls the user by his or her name
while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
#The "while" loop will continue until the number is guessed correctly or the maximum of 6 guesses have been met.
    guessesTaken += 1
#Each time the user makes a guess, this will add 1 to the variable that is responsible for counting how many guesses the user have used.
    if guess < number:
        print('Your guess is too low.')
#This statement makes sure that if the number that the user have input is low to inform the user that it is in fact low.
    if guess > number:
        print('Your guess is too high.')
#This statement makes sure that if the number that the user have input is high to inform the user that it is in fact high.
    if guess == number:
        break
#This statement makes sure that if the number that the user have input is the correct number to break the loop
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
#This statement makes sure that outside the "while" loop if the number was guesses correctly by the user to inform the user and converts the number to a string to print out.
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
#This statement makes sure that outside the "while" loop if the number is not the correct one and converts the original generated number into a string to be printed out.