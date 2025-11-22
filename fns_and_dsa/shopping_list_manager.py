def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

shopping_list = []

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please try again.")
        continue
    
    if choice == 1:
        item = input("Enter the item name: ")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")
    
    elif choice == 2:
        item = input("Enter the item name: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")
        else:
            print(f"{item} not found in the shopping list.")
    
    elif choice == 3:
        print("Shopping List:")
        if len(shopping_list) == 0:
            print("The shopping list is empty.")
        else:
            for item in shopping_list:
                print(f"- {item}")
    
    elif choice == 4:
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")