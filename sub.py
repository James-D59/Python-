#subprocessor to run files from this file
import subprocess
import os

os.system('cls')

# Funnction to run a selected Python program
def run_file(filename):
    try:
        #run the file
        subprocess.run(['python', filename ], check=True)
    except subprocess.CalledProcessError:
        print(f'Error: Cound not run {filename}.')


# main function
def main_menu():
    while True:
        print('\n--- Main Menu ---')
        print('1. Clocks ')
        print('2. Hangman ')
        print('3. Palindrome')
        print('4. Password Generator')
        print('5. Random Number')
        print('6. Rock Paper Scissors')
        print('7. To Do List')
        print('8. Quit ')

        # get choice
        choice = input('Choose an option (1-8): ')

        if choice == '1':
            run_file('clocks.py')
        elif choice == '2':
            run_file('hangman.py')
        elif choice == '3':
            run_file('palindrone.py')
        elif choice == '4':
            run_file('password_generator.py')
        elif choice == '5':
            run_file('random_num.py')
        elif choice == '6':
            run_file('rock_paper_scissors.py')
        elif choice == '7':
            run_file('to_do_list_1')
        elif choice == '8':
            break
        else:
            print('Invalid option please select from 1-8.')


#run profram
main_menu()