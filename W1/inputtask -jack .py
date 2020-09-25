people  = ["Jack", "Jill", "James", "Joriginalname"]
drinks = ["Vodka", "Stronger Vodka", "Absinthe", "Morgue"]

# Base menu that shows initially
def menu():
    print("\nSelect an option by entering a number:")
    print("[1] Get all people")
    print("[2] Get all drinks")
    print("[3] Exit")
    print("=" * 20)
    answer = input("\nEnter your selection: \n\n")
    response(int(answer))

# After input is given, this code runs to ask if they want to do sumting else
def run_again():
    print("\nDo you wish to choose another option?")
    answer = input("Enter 'yes' to continue or 'no' to quit: ")
    if answer.lower() == "yes":
        menu()
    if answer.lower() == "no":
        quit()
    else:
        print("\nUnrecognised response")
        run_again()

# Process the users response
def response(answer):
    global drinks
    global people
    if answer == 3:
        quit()
    elif answer == 2:
        print(*drinks, sep = "\n")
        run_again()
    elif answer == 1:
        print(*people, sep = "\n")
        run_again()
    else:
        print("Unrecognised command")
        run_again()

# Call the program when we run the app initially
menu()