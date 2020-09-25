import sys
args = sys.argv
# Define data
# Expected commands
GET_PEOPLE_ARG = 'get-people'
GET_DRINKS_ARG = 'get-drinks'
people = ['Johnny', 'Malik', 'Khalid', 'Suman']
drinks = ['Tea', 'Mocha', 'Coffee', 'Americano']
# Check args - assumming/expecting only one command at a time
if len(args) < 2:
    print("I don't know what you want me to do")
    exit()
if len(args) > 2:
    print('I can only do one thing at a time, what do you want me to do?')
    exit()
# Table outut helper funcs
def print_table(title, data):
    width = get_table_width(title, data)
    print_header(title, width)
    for item in data:
        print(f'| {item}')
    print_separator(width)
def print_header(title, width):
    print_separator(width)
    print(f'| {title}')
    print_separator(width)
def print_separator(width):
    print(f"+{'=' * width}")
def get_table_width(title, data):
    longest = len(title)
    additional_spacing = 2
    for item in data:
        if len(item) > longest:
            longest = len(item)
    return longest + additional_spacing
# Handle arguments
command = args[1]
if command == GET_PEOPLE_ARG:
    print_table('People', people)
elif command == GET_DRINKS_ARG:
    print_table('Drinks With A Really Long Title', drinks)
else:
    print(f'"{command}" is not an command that I recognise.')