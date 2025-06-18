#arrows
import os
from pynput import keyboard 

os.system("cls")


def on_press(key):
    try:
        #check for q
        if key.char == "q":
            print("Exiting Program...")
            return False #stop listerner
    except AttributeError:
        pass
        
    #check for arrow keys
    if key == keyboard.Key.up:
        print("Up")
    elif key == keyboard.Key.down:
        print("Down")
    elif key == keyboard.Key.left:
        print("Left")
    elif key == keyboard.Key.right:
        print("Right")





# prompt user
print(" Press arrow keys! Press q to exit...")




with keyboard.Listener(on_press =on_press) as listener: #create listerner object that listens for keyboard events
    #start the listener and wait for it to finish
    listener.join()
