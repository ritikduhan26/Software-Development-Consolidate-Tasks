# Consolidate Task 3 that help user to Calculate Area of Rectangle and Circle

print("Hey Calculate the area of Rectangle  and Circle")

while True:
    print("Choose a shape")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Exit")

    choose = input("Enter your choice (1, 2, 3) ")

    # Conditional Statement

    if choose == "1":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print("The area of the rectangle is", area)

    elif choose == "2":
        radius = float(input("Enter the radius   "))
        area = 3.14 * radius * radius
        print("The area of the circle is", area)
        
    elif choose == "3":
        print("Exit")
        break 
    
    else:
        print("You Entered a Wrong Number")
