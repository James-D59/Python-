#file manager

import os

os.system('cls')




#function to create and save a file
def create_file():
    #prompt for file details
    text = input('Enter the text you want to save in the file: ')
    file_name = input('Enter the filename ending in .txt (e.g. myfile.txt): ')
    file_location = input('Enter the file location (e.g. C:/Users/DITTJA/): ')

    #ensure directory exists or create it
    if not os.path.exists(file_location):
        os.makedirs(file_location)

    # full file path
    file_path = os.path.join(file_location, file_name)

    #wrtite the text to the file
    with open(file_path, 'w') as file:
        file.write(text)
    print(f'File "{file_name}" saved successfully at {file_location}')


# function to open and read a file
def open_file():
    #promt the user for file details
    file_name = input('Enter the filename to open ending in .txt (e.g. myfile.txt): ')
    file_location = input('Enter the file location (e.g. C:/Users/DITTJA/): ')

    #get the full path
    file_path = os.path.join(file_location, file_name)

    #check if file exists
    if os.path.exists(file_path):
        #read treh output of the file (r= will make it open to read and write)
        with open(file_path, 'r+') as file:
            #print contents
            print('\nFile Contents: ')
            print(file.read())
    else:
        print(f'File "{file_name}" not found at {file_location}.')
        





# main function
def file_manager():
    while True:
        print('\n----Flike Manager ---')
        print('1. Create and save a file')
        print('2. Open and read a file')
        print('3. Quit')

    #get selection
        choice = input('Choose an option (1/2/3): ')

        if choice =='1':
            create_file()
        elif choice == '2':
            open_file()
        elif choice == '3':
             print('Exiting the program. Later Dude!')
             break
        else:
            print('Invalid selection. Please choose 1, 2, or 3.')




#run the program
file_manager()
