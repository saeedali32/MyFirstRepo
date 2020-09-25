import sys 
args = sys.argv
print(args)


#Define data 
GET_PEOPLE_ARG = "get-people"
GET_DRINKS_ARG = "get-drinks" 
GET_ALCO_DRINKS_ARG = "get-alco-drinks"

people = ["Obama", "Trump", "Boris"]
drinks = ["Coke", "pepsi", "fanta"]
alco_drinks = ["JD", "Vodka", "Rum"]



#if len(args) < 2:
#    print("What do you want me to do, I'm unsure")
 #   exit()
#if len(args) > 2: 
   # print("I can only do one thing at a time, what?")
   # exit()

command = args[0]
if command == GET_PEOPLE_ARG:
    for person in people:
        print(person)
elif command == GET_DRINKS_ARG:
    for drink in drinks:
        print(drink)
else:
    print("I do not recognise command")



def print_header(title):
    print("|  " + title.upper())

def print_row(row):
    print("|  " + row)

def print_outline():
    print("+=======================================+")

#people = ["Obama", "Trump", "Boris"]
#drinks = ["Coke", "pepsi", "fanta"]

print_outline()
print_header("people")


age = 23

def age_check(age):
    if age < 18:
        print("you can have any drink from " + str(drinks))
    else:
        print("you can have any drink from " + str(drinks) + "and" + str(alco_drinks))

age_check(17)


user_input = input("How old are you?")
inputting = user_input

if inputting >= "18":
    print("you can have any drink from " + str(drinks) + "and" + str(alco_drinks))
elif inputting <= "18": 
    print(drinks)
elif inputting == "3":
    print("exit")
else: 
    print("Have a good day!, See you again soon!")