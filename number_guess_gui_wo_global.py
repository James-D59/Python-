#importing from tkinter for GUI
from tkinter import *

# Import the os module/library
import os
# Import the random library
import random





# Create a play again function
def reset_game(guess_entry, result_label, submit_button, play_again_button, state):
	#set our global variables

	#generate a random number and assign it to a variable
	state ['number_to_guess'] = random.randint(1,10)
	#reset number of giuesses
	state ['number_to_guesses'] = 0

	#delete result label
	result_label.config(text="")
	#clear the entry box
	guess_entry.delete(0, END)
	#setthe submit button back tonormal
	submit_button.config(state=NORMAL)
	# hide th eplay button..again
	play_again_button.pack_forget()




# Create our main game function
def check_guess(guess_entry, result_label, submit_button, play_again_button, state):
	

	# Try/except block
	try:
		guess = int(guess_entry.get())
		state ['number_of_guesses'] += 1 
		# Create some logic to check the guess
		if guess < state ['number_to_guess']:
			result_label.config(text="Too Low! - Try Again!")
			guess_entry.delete(0, END)

			
		elif guess > state ['number_to_guess']:
			result_label.config(text="Too High! - Try Again!")
			guess_entry.delete(0, END)
			

		else:
			result_label.config(text=f"Correct! The number was {state ['number_to_guess']} and you guessed it in {state ['number_to_guesses']} guesses!")
			#disable the guess button
			#enable the play again button
			submit_button.config(state=DISABLED)
			play_again_button.pack()


	except ValueError:
		result_label.config(text="Invalid Input, PLease enter a Number")

	

def setup_gui():


	# Clear The Screen
	os.system("clear")


	#create window
	root = Tk()
	#add a title
	root.title("Guessing Game")
	# set size of app
	root.geometry('500x350')

	# setting up the game state
	state = {'number_to_guess':None, 'number_of_guesses':0}


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
	submit_button = Button(root, text="Submit Guess", command=lambda: check_guess(guess_entry, result_label, submit_button, play_again_button, state))
	submit_button.pack(pady=20)

	play_again_button = Button(root, text="Play Again?",command = lambda: reset_game(guess_entry, result_label, submit_button, play_again_button, state))
	play_again_button.pack()
	#Hide this button
	play_again_button.pack_forget()



	#on start reset teh game
	reset_game(guess_entry, result_label, submit_button, play_again_button, state)

	#start the app
	root.mainloop()

#call our main function
setup_gui()



























