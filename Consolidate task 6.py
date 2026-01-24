# Software Development Consolidate Task Unit - 6  To Do List Manager

# List to store task enetered by the user

tasks = []

# This is the function to add tasks

def addTask():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "status": "Pending"})
    print(" Your task added successfully\n")

# Function to view tasks

def viewTasks():
    if not tasks:
        print("No task found\n")
    else:
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['task']} - {t['status']}")
        print()

# FUnction to mark a taks "Completed"

def completeTask():
    viewTasks()
    if tasks:
        num = int(input("Enter any task number to mark your task as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["status"] = "Completed"
            print("Your task marked as completed\n")
        else:
            print("You eneterd a wrong number\n")



while True:
    print("To  Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    # This helps to get user choice

    choose = input("Enter any Number: ")

    # Calling function 

    if choose == "1":
        addTask()
    elif choose == "2":
        viewTasks()
    elif choose == "3":
        completeTask()
    elif choose == "4":
        print(" Bye Bye")
        break
    else:
        print("You Entered a Wong Number Please try agaian  \n")
