if __name__ == "__main__": 

    while True:
        print_menu()
        option = get_selection('Enter your selection:')
        if not option:
            print("That option is invalid, Please only use numbers to select from the menue")
            wait()
            continue 

        # Handle arguments
        if option == GET_PEOPLE_ARG:
            print_table('People', people)
            wait()

        elif option == GET_DRINKS_ARG:
            print_table('Drinks', drinks)
            wait()

        elif option == EXIT_ARG:
            print(f'Thank you for using {APP_NAME}')
            wait()
            exit()

        elif option == VIEW_DRINK:
            un_pack(peoplesDrinks)
            wait()

        elif option == ADD_PEOPLE:
            new_name = input("Please enter new name: ")
            people.append(new_name)
            print(f'"{new_name}" has been added')
            done()
        
            
        elif option == ADD_DRINK:
            new_drink = input("Enter new drink: ")
            drinks.append(new_drink)
            print(f'"{new_drink}" has been added')
            done()

        else:
            print(f'"{option}" is not an command that I recognise.')
            wait()