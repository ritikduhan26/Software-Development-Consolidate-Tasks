# This will help to import the time module from the Python library 

import time   

# Ask the user to press Enter to start the timer

input("Press Enter to start the timer")

print("The timer has started")

# Record the current time and the start time

strttime = time.time()

# Ask the user to press enter to stop the timer

input("Press Enter to stop the timer")

# Record the current time as the end time

endtime = time.time()


# Calculate difference between the end time and the start time

timediff = endtime - strttime

# Show the total time taken in seconds, and round(timediff, 2) is used to display the total time with only two decimal.

print("Total time is", round(timediff, 2), "seconds") # https://docs.python.org/3/library/functions.html#round


# Stop the program 

input("Press Enter to exit")
