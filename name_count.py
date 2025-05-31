#input a name and count out the letters

#I always like to clear screen after use 
import os
os.system("clear")


name = input("Enter your Name: ")

print(f'Your Name has {len(name.replace(" ",""))} letters!')

'''
I originally had the following code
print(f'Your Name has {len(name} characters!')
but that gave me a count including the spaces. I had to google how to remove the spaces using the .replace() command
There were other options, but this was the easiest and cleanest way
'''

