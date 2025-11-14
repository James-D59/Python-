#math flashcard game

import random
import os


#function to generaste math problem
def generate_flashcard(operation):
    # generate 2 random numbers
    num1 = random.randint (1,100)
    num2 = random.randint (1,100)

    #logic to do the thing
    if operation == 'addition':
        correct_answer = num1 + num2
        question = f'{num1} + {num2} = ?'

    elif operation == 'subtraction':
        correct_answer = num1 - num2
        question = f'{num1} - {num2} = ?'

    elif operation == 'multiplication':
        correct_answer = num1 * num2
        question = f'{num1} * {num2} = ?'   

    elif operation == 'division':
        #ensure teh second number is not zero and that num1 is divisable by num2
        while num2 == 0 or num1 % num2 != 0: #chesking to see if there is any remainders
            #get new numbers
            num1 = random.randint (1,100)
            num2 = random.randint (1,100)

        correct_answer = num1 // num2
        question = f'{num1} / {num2} = ?'

    #return results
    return question, correct_answer


# Main menu function
def main_menu():
    # clear teh screen
    #os.system('cls')
    # create a menu
    print('\n---Math Flashcard App---')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Quit')
    
    # get user choice
    choice = input('Choose an option (1-5): ')
    return choice




# function to create flashcard session
def flashcard_session(operation):
    while True:
        #clear teh screen
        os.system('cls')
        question, correct_answer =generate_flashcard(operation)

        #print question
        print(f'\nFlashcard: {question}')

        #prompt user for answer
        user_answer = int(input('Your answer: '))

        #error handling
        try:
            user_answer = int(user_answer)
        except ValueError:
            print('Invalid input. Please enter a valid number.')



        #answer solution
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'Wrong! The correct answer is {correct_answer}')

        next_step = input('\nWould you like another flashcard (y/n)?').lower()

        if next_step == 'n':
            break


# Main function
def math_flashcard_app():
    while True:
        #call teh menu
        choice = main_menu()

        #logic to determine the choice
        if choice == "1":
            flashcard_session("addition")
        elif choice == '2':
            flashcard_session('subtraction')
        elif choice == '3':
            flashcard_session('multiplication')
        elif choice == '4':
            flashcard_session('division')
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice, please try again.')


#run the app
math_flashcard_app()



