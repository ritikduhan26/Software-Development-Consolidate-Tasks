#  Consolidate Task 4

# Import the csv module to work with CSV files
import csv

# It will create list to store inventory items
inventory = []

# This is a CSV file to save  data
invenfile = "inventory.csv"

# this function helps to load inventory 

def loadinven():
    try:
        
        file = open(invenfile, "r") # Open CSV file

        reader = csv.reader(file)           # Create reader object

        next(reader)  # Skip the header row


        # This loop will read row line by line from the file
        for row in reader:
            inventory.append({
                "name": row[0],              
                "quantity": int(row[1]),    
                "price": float(row[2])      
            })
        file.close()

    except:
        # If the does'r exits, it will start with empty inventory
        print("No inventory file found. Starting new inventory.")


# Function to save inventory 

def save_inventory():
    # Open the CSV file
    file = open(invenfile, "w", newline="")

    writer = csv.writer(file)

    # header row
    writer.writerow(["name", "quantity", "price"])

    # Write each product to the file
    for item in inventory:
        writer.writerow([item["name"], item["quantity"], item["price"]])

    # Close the file
    file.close()


# Function to add a new product

def add_product():
    # take input from the user
    name = input("Add product name: ")
    quantity = int(input("Add quantity: "))
    price = float(input("Add price: "))

    # Add product details to inventory list
    inventory.append({
        "name": name,
        "quantity": quantity,
        "price": price
    })

    print("Your product is added successfully!")


# Function to display inventory
def showinven():
    # Check if inventory is empty
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("\nInventory List:")
        for item in inventory:
            print(
                "Name:", item["name"],
                "| Quantity:", item["quantity"],
                "| Price:", item["price"]
            )


# Main Program Starts Here

# Load existing inventory 
loadinven()

# Display menu until user exits
while True:
    print("\n--- Inventory Menu ---")
    print("1. Add Product")
    print("2. Show Inventory")
    print("3. Save and Exit")

    choose = input("Choose an option to add: ")

    if choose == "1":
        add_product()
    elif choose == "2":
        showinven()
    elif choose == "3":
        save_inventory()
        print("Your product saved in Inventory saved.")
        break
    else:
        print("You enetered a wrong Number. Please try again.")

