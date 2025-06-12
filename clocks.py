import time
from datetime import datetime
import os
import threading
from zoneinfo import ZoneInfo #pip zoneinfo if needed



def clear_screen():
    os.system('cls')

#set up hitting enter to quit
def input_thread(stop_event):
    input()
    stop_event.set()

#print current time
#current_time = time.strftime("%I:%M:%S")  #("%I:%M:%S %p") to add am or pm
#print(current_time)

def main():

    #set up timesones
    time_zones = {'1': ('Eastern Time', 'America/New_York'),'2': ('Central Time', 'America/Chicago'),'3': ('Pacific Time', 'America/Los_Angeles')}
    #prompt to pick the time zone
    print('Select a Time Zone:')
    #loop through time zone dictionary
    for key, (name, _) in time_zones.items():
        print(f"{key}, {name}")

    #assign selection to a variable
    choice = input("Enter the number of your choice: ").strip()

    #error handling for choice selection
    if choice not in time_zones:
        print('Invalid Result. Defaulting to Central Time.')
        tz_name = "America/Chicago"
        tz_display_name = "Central Time"
    else:
        tz_display_name, tz_name = time_zones[choice]

    #create an event to stop the clock/program
    stop_event = threading.Event()
    #start the input thread
    thread = threading.Thread(target=input_thread, args=(stop_event, ))
    thread.daemon = True
    thread.start()



    #Loop to update our time in seconds until enter is pressed
    while not stop_event.is_set():
        clear_screen()
        #get current time
        #current_time = time.strftime("%I:%M:%S") this was to get current time
        current_time = datetime.now(ZoneInfo(tz_name)).strftime("%I:%M:%S %p")
        print(f"The Current time is: {current_time} - {tz_display_name}") 
        #prompt user to stop clock
        print('Press enter to stop the clock...')
        #run loop once per second
        time.sleep(1)

    # print an end message
    print('Clock Stopped...')



clear_screen


main()












