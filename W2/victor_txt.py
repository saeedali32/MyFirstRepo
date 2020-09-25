elif user_menu_input == '6':
        person_favourite()
        global y
        for x, y in favourite_drinks.items():
            print(x, ' - ', y)
            favourite_drinks_file = open('./favourites.txt', 'w')
            favourite_drinks_file.write(f'{x} - {y}')
            favourite_drinks_file.close()