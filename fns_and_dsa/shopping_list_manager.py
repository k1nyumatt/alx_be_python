# Shopping List Manager

def display_menu():
    """Display the shopping list menu options"""
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

# Initialize the shopping list array
shopping_list = []

# Main program loop
while True:
    # Call display_menu function
    display_menu()
    
    # Get user choice as a number
    choice = int(input("Enter your choice (1-4): "))
    
    # Option 1: Add an item
    if choice == 1:
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")
    
    # Option 2: Remove an item
    elif choice == 2:
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the list.")
        else:
            print(f"'{item}' not found in the list.")
    
    # Option 3: View the list
    elif choice == 3:
        if shopping_list:
            print("\nYour Shopping List:")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
        else:
            print("Your shopping list is empty.")
    
    # Option 4: Exit
    elif choice == 4:
        print("Goodbye! Happy shopping!")
        break
    
    # Handle invalid choices
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")