#import the os library for CMD
import os

os.system("cls")

def is_palindrome(string):
    #remove space and convert to lowercase and strip notation
    cleaned_string = ""
    #loop through user input
    for character in string:
        # chich if character is a character
        if character.isalnum():
            cleaned_string += character.lower()
 
 #shorthand for teh abopve code (all on one line of code)
 # cleaned_string = "".join(character.lower() for character in string if character.isalnum())
   

    return cleaned_string == cleaned_string[::-1]


user_input = input("Enter a word or phrase to check if it's a palindrome: ")
#user_input == user_input[::-1]

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is NOT a palindrome!")




#print(is_palindrome(user_input))

'''
#slice = [start:end:step]  this will reverse teh word
if user_input == user_input[::-1]:
    print(f"{user_input} is a palindrome!")

else:
    print(is_palindrome(user_input))
'''