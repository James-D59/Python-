import os
import random


os.system('cls')

#create a list of words
word_list = ['python', "java", "javascript", "ruby", "program", "coding", "developer", "variable", "string", "print", "function"]

#select random word from list
def get_random_word():
    return random.choice(word_list)

#display the current state of the guessed word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


#main game logic
def play_hangman():
    word = get_random_word()
    word_length = len(word)  #get the word length

    #keep track of guesses and guessed letters
    #use a set since sets dont allow duplicates so the same letter can't be guessed more that once
    guessed_letters = set() #letters player guessed correct
    incorrect_guesses = set()
    lives = 6 #number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print(f" The word has {word_length} letters.")


    #main game loop
    while lives > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Incorrect guesses: {', ' .join(incorrect_guesses)}")
        print(f"Lives Remaining: {lives}")

    #prompt user for guess
        guess = input("Guess a letter: ".lower())

    #validate the guess
        if len(guess) != 1 or not guess.isalpha():
            os.system('cls')
            print("Please eneter a single letter.")
            continue
#check if letter already guess
        if guess in guessed_letters or guess in incorrect_guesses:
            os.system('cls')
            print(f"You have already guessed {guess}. Try a different letter dummy!")
            continue
        #check if guess is correct
        if guess in word:
            os.system('cls')
            guessed_letters.add(guess)
            print(f"Good Guess! '{guess}' is in the word.")
        else:
            os.system('cls')
            incorrect_guesses.add(guess)
            lives -= 1  #remove a life
            print(f"Wrong! '{guess}' is not in the word dummy.")

        #check if player has guesed the word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongrats! You have guessed the word: {word}")
            break

#if player runs out of guess
    if lives == 0:
        print(f"\n You ran out of guesses! The word was: {word}")

play_hangman()


















