#Consolidate Task 8
# Function to find Fibonacci number
def findnum(n):

# Return 0 if number is 0 or less
    if n <= 0:
        return 0

# Return 1 if number is 1
    if n == 1:
        return 1

 # First two Fibonacci numbers
    a, b = 0, 1

# Calculate Fibonacci numbers 
    for _ in range(2, n + 1):
        a, b = b, a + b

# Return the result
    return b


# Take input from the user
n = int(input("Enter which Fibonacci number you want: "))

# Check for negative input
if n < 0:
    print("Enter a number greater than zero.")
else:
# Print Fibonacci number
    print("The number is:", findnum(n))
