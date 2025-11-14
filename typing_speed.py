#typing speed Test app
import time
import random
import os

os.system ("cls")


# list of sentances for teh typing test
sentences = [
    "The quick brown fox jumped over the lazy dog sleeping dog.",
    "Python is an easy to learn programming language.",
    "Typing speed tests are a stupid waste of time.",
    "Consistant practice is key to mastering any skill.",
    "Look out, there is a monster behind you!"
]


#function to calculate words per minute (wpm)
def calculate_wpm(start_time, end_time, typed_text):
    #calculate the time in seconds that it took to type
    time_taken = end_time - start_time #in seconds
    #calculate the number of words
    num_words = len(typed_text.split())
    # Calculate the WPM
    wpm = (num_words / time_taken ) * 60 #words per minute formula
    #return teh results
    return(round(wpm, 2))




# function to run tehg typing test
def typing_speed_test():
    #choose a random sentence from list
    sentence = random.choice(sentences)

    print('\n---Typing Speed Test ---')
    print('Type the following sentence as fast as you can: ')
    print(f'\n{sentence}\n')

    #tell the user to hit enter to start
    input("Press Enter when you are ready to start...")

    #start the timer
    start_time = time.time()

    # prompt user to start typing
    typed_text = input("\nStart typing here: (hit enter when finished)\n")

    # Get the end time
    end_time = time.time()

    #calculate WPM
    wpm = calculate_wpm(start_time, end_time, typed_text)

    #output the results
    if typed_text == sentence:
        print(f'Grat Job! Your typing sepped is {wpm} words per minute!')
    else:
        print(f'Your typing speed is {wpm} words per minute, but there were some mistakes in your typing.')





def main():
    while True:
        #clear teh screen
        os.system("cls")
        #start the test
        typing_speed_test()
        #ask if user wants to try again
        retry = input("\nWould you like to try again? (y/n?)").lower()
        if retry != "y":
            print("Thanks for using the Typing Speed Test! Later Dude!")
            break




#run the app
main()








