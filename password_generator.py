import os
import string
import random



os.system("cls")


def validate_password(password):
    #check for password rules
    if len(password) < 8:
        return False, "Passowrd must be at least 8 characters long."
    #check for digits
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number"
    #check for lowercase letters
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."
     #check for uppercase letters
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    #check for special characters
    if not any(char in string.punctuation for char in password):
        return False, "Password must contain at least one speacial character."
    #return true if all the rules oar true
    return True, "Password is Strong!"


#generate password
def generate_password(length):
    while True:
        #ensure we meet basic criteria 
        password = [
            random.choice(string.ascii_lowercase), #at least one lowercase
            random.choice(string.ascii_uppercase), #at least one uppercase
            random.choice(string.digits), #at least one numebr
            random.choice(string.punctuation), #at least one special character
        ]
        #fill in the rest of the password with random characters from all sets
        #get remaining count
        remaining_length = length - 4 
        password += random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=remaining_length)
        #shuffle list
        random.shuffle(password)

#convert list to a string using join()
        password = ''.join(password)

        # validate
        is_valid, message = validate_password(password)
        if is_valid:
            return password




#prompt user
def password_generator():
    #get password lenght
    while True:
        try:
            length = int(input("Enter the desired password length (minumum of 8 characters): "))
            if length < 8:
                print("Password must be at least 8 characters.")
                continue 
            break
        
        except ValueError:
            print("Invalid input. Please enter a number for characters.")


    password = generate_password(length)
    print(f"Generated Password: {password}")
    print("This Password is Strong!!")









password_generator()












