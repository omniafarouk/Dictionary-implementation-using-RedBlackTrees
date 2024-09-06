from dictionary import Dictionary

filename = "Dictionary.txt"
dictionary = Dictionary(filename)

while True:
    print("\nChoose an option:")
    print("1. Insert Word")
    print("2. Look-up a Word")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        dictionary.insert()
        dictionary.save_to_file(filename)
    elif choice == '2':
        dictionary.Look_up()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
