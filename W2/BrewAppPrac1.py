#Define data 
GET_PEOPLE_ARG = 1
GET_DRINKS_ARG = 2 
ADD_PEOPLE = 3
ADD_DRINK = 4
VIEW_DRINK = 5 
EXIT_ARG = 6

from table import print_header, print_separator, print_table, get_table_width

APP_NAME = 'Brew App'
MENU = f'''
Welcome to {APP_NAME} v0.1!
Please, select an option by entering a number:
[1] Get all people
[2] Get all drinks
[3] Add new name
[4] Add new drink
[5] View drink options 
[6] Exit
'''

peoplesDrinks = {
"1": {"Name" : "Obama", "Drink" : "Coke"},
"2": {"Name" : "Trump", "Drink" : "Pepsi"},
"3": {"Name" : "Boris", "Drink" : "Fanta"}
}

def un_pack(data):
    for x in data.values():
        name = x.get("Name")
        drink = x.get("Drink")
        print(name + " likes " + drink)
        

people = ["Obama", "Trump", "Boris"]
drinks = ["Coke", "pepsi", "fanta"]

#Tidy Table - All being imported at top 

# def print_table(title, data):
#     width = get_table_width(title, data)
#     print_header(title, width)
#     for item in data:
#         print(f'| {item}')
#     print_separator(width)

# def print_header(title, width):
#     print_separator(width)
#     print(f'| {title}')
#     print_separator(width)

# def print_separator(width):
#     print(f"+{'=' * width}")

# def get_table_width(title, data):
#     longest = len(title)
#     additional_spacing = 2
#     for item in data:
#         if len(item) > longest:
#             longest = len(item)
#     return longest + additional_spacing

def print_menu():
    print(MENU)

def get_selection(message):
        try:
            return int(input(f'{message} \n'))
        except ValueError:
            return False

def wait():
    input('Press ENTER to return to the menu')

def done():
    print("Thank you")
    wait()

# while True:
#     print_menu()
#     option = get_selection('Enter your selection:')
#     if not option:
#         print("That option is invalid, Please only use numbers to select from the menue")
#         wait()
#         continue 

#     # Handle arguments
#     if option == GET_PEOPLE_ARG:
#         print_table('People', people)
#         wait()

#     elif option == GET_DRINKS_ARG:
#         print_table('Drinks', drinks)
#         wait()

#     elif option == EXIT_ARG:
#         print(f'Thank you for using {APP_NAME}')
#         wait()
#         exit()

#     elif option == VIEW_DRINK:
#         un_pack(peoplesDrinks)
#         wait()

#     elif option == ADD_PEOPLE:
#         new_name = input("Please enter new name: ")
#         people.append(new_name)
#         print(f'"{new_name}" has been added')
#         done()
    
        
#     elif option == ADD_DRINK:
#         new_drink = input("Enter new drink: ")
#         drinks.append(new_drink)
#         print(f'"{new_drink}" has been added')
#         done()

#     else:
#         print(f'"{option}" is not an command that I recognise.')
#         wait()

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