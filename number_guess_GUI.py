#importing from tkinter for GUI
from tkinter import *

# Import the os module/library
import os
# Import the random library
import random


#initialize the game state variables
number_to_guess = None
number_of_guesses = 0



# Create a play again function
def reset_game():
	#set our global variables
	global number_to_guess, number_of_guesses
	#generate a random number and assign it to a variable
	number_to_guess = random.randint(1,10)
	#reset number of giuesses
	number_of_guesses = 0

	#delete result label
	result_label.config(text="")
	#clear the entry box
	guess_entry.delete(0, END)
	#setthe submit button back tonormal
	submit_button.config(state=NORMAL)
	# hide th eplay button..again
	play_again_button.pack_forget()




# Create our main game function
def check_guess():
	global number_of_guesses





	# Try/except block
	try:
		guess = int(guess_entry.get())
		number_of_guesses += 1 
		# Create some logic to check the guess
		if guess < number_to_guess:
			result_label.config(text="Too Low! - Try Again!")
			guess_entry.delete(0, END)

			
		elif guess > number_to_guess:
			result_label.config(text="Too High! - Try Again!")
			guess_entry.delete(0, END)
			

		else:
			result_label.config(text=f"Correct! The number was {number_to_guess} and you guessed it in {number_of_guesses} guesses!")
			#disable the guess button
			#enable the play again button
			submit_button.config(state=DISABLED)
			play_again_button.pack()


	except ValueError:
		result_label.config(text="Invalid Input, PLease enter a Number")

	

def setup_gui():
	#make all of the widgets global
	global result_label, guess_entry, submit_button, play_again_button

	# Clear The Screen
	os.system("clear")


	#create window
	root = Tk()
	#add a title
	root.title("Guessing Game")
	# set size of app
	root.geometry('500x350')

	#Create a label
	instruction_label = Label(root, text="Guess a Number between 1 and 10", font=("Helvetica", 18))
	instruction_label.pack(pady=20)

	#Create an entry box
	guess_entry = Entry(root, font=("Helvetica", 18))
	guess_entry.pack(pady=10)

	#Create a another label
	result_label = Label(root, text="")
	result_label.pack(pady=20)

	#Create some buttons
	submit_button = Button(root, text="Submit Guess", command=check_guess)
	submit_button.pack(pady=20)

	play_again_button = Button(root, text="Play Again?",command = reset_game)
	play_again_button.pack()
	#Hide this button
	play_again_button.pack_forget()



	#on start reset teh game
	reset_game()

	#start the app
	root.mainloop()

#call our main function
setup_gui()



























