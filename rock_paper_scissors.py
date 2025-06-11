#import the os library for CMD
import os
#import the random library
import random


os.system("cls")


#ask to play agaion
def play_again():
	while True:
		user_input = input("Do you want to play again? (yes/no): ").lower()
		if user_input in ["yes", "no"]:
			return user_input == "yes"
		else:
			print("Invalid input ender yes or no")





def determine_winner(user_choice, computer_choice):
	#make the logic to figure out who wins
	if user_choice == computer_choice:
		return "It's a tie!"
	elif (user_choice == "rock" and computer_choice == "scissors") or \
		(user_choice == "paper" and computer_choice == "rock") or \
		(user_choice == "scissors" and computer_choice == "paper"):
		return "You Win!!"
	else:
		return "Computer Wins!"



def get_computer_choice():
#have the computer pick its choice using a dictionary
	choices = ["rock", "paper", "scissors"]
	return random.choice(choices)


def get_user_choice(): #using a dictionary with key value pairs
	choices = {1:"rock", 2:"paper", 3:"scissors"}
	try:
		user_input = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
		if user_input in choices:
			return choices[user_input]
		else:
			print("Invalid choice, please try again!")
			return get_user_choice()

	except ValueError:
		print("Invalid input, enter a value between 1 and 3!")
		return get_user_choice() #this will re-ask the choice if an invalid input is given

#setup game
def play_game():
	while True: #this makes the game reset automatically.....forever
		os.system("cls")
		user_choice = get_user_choice()
		#get computer choice
		computer_choice = get_computer_choice()

		#outputs on screen
		print(f"You chose: {user_choice}")
		print(f"The computer chose: {computer_choice}")

		#results
		result = determine_winner(user_choice, computer_choice)
		print(result)

		if not play_again():
			print("Thanks for playing! Goodbye!")
			break


play_game()




