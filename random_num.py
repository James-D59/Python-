#import the os library for CMD
import os
#import the random library
import random


#create a play agaion function
def play_again():
    #prompt user
    again = input('Would you like to play again? y/n ')
    #logic to figure out what to do
    if again == "y" or again == "yes":
        game()
    else :
        print('Thanks for playing!')
        return  


#Create main game function
def game():
    #Create a variable to track the number of guess
    number_of_guesses = 0
    correct = False

    os.system("cls")


    #Generate a random number
    #one way to do it is print(random.randint(1,10))

    #Generate a random number and assign it to a variable
    number_to_guess = random.randint(1,10)

    #Get user input
    print("Guess a number between 1 and 10: ")




    '''
    guess = int(input("Enter your Guess: ")) #add in int() to the fron to make sure only numbers canm be entered

    print(f"You Guessed {guess}")

    I did this on my own and it worked! next is the tutorial way to do it
    if number_to_guess ==guess:
        print("You got it!")
    else:
        print(f"You are wrong! The correct number was {number_to_guess}.")
    '''
    #Guessing loop
    while correct == False:
    #Try/except block
        try:
            guess = int(input("Enter your Guess: "))
            print(f"You Guessed {guess}")
        except:
            print("Only enter a number. Game Over!")
            return #this will end the program, could also enter game() to restart the game
        '''
        except Exception as e:
           print("Only enter a number!")
            print(e)  #this will list the error on the screen
        '''
        # Create some logic to check the guess and increment the number of guesses
        if guess < number_to_guess:
            print("Too low! Try Again!")
            number_of_guesses += 1
        elif guess > number_to_guess:
            print('Too high! Try again!')
            number_of_guesses += 1

        elif guess == number_to_guess:
            number_of_guesses += 1
            print(f'Correct the number was {number_to_guess} and you guessed it in {number_of_guesses}!')
            #set correct to true
            correct = True
            # run play again function to see if player wants to play again
            play_again()
#Call our gamne function
game()





















