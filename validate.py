import os
import string



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
    




def show_password_rules():
    print("Password Rules:")
    print("1. Must be at least 8 characters long.")
    print("2. Must contain at least one digit (0-9)")
    print("3. Must contain at least one lowercase letter (a-z)")
    print("4. Must contain at least one uppercase letter (A-Z)")
    print("5. Must contain at least one special character (!, @, #, $, etc.)")
    print()

def password_validator():
    show_password_rules()
    password = input("Please enter your password: ")
#validate the password
    is_valid, message = validate_password(password)
#return result
    if is_valid:
        print("Success:", message)
    else:
        print("Validation Failed:", message)

password_validator()


