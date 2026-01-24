# Consolidate Task 8


# Function that returns Fibonacci using recursion

def findnum(place):

    # this is the  conditions
    if place <= 0:
        return 0
    if place == 1:
        return 1

    # Recursive formula to find 
    return findnum(place - 1) + findnum(place - 2)


# Main part of program
n = int(input("Enter which Fibonacci number you want:"))

if n < 0:
    print("Please enter a number greater that Zero.")
else:
    result = findnum(n)
    print("The number is :", result)
