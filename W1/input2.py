people = ["Obama", "Trump", "Boris"]
drinks = ["Coke", "pepsi", "fanta"]

print("Welcome to BrIW v0.1!")
user_input = input("Please select an option from the list below by entering a number:  \n [1] Get all people  \n [2] Get all drinks \n [3] Exit")
inputting = user_input

if inputting == "1":
    print(people)
elif inputting == "2": 
    print(drinks)
elif inputting == "3":
    print("exit")
else: 
    print("Have a good day!, See you again soon!")
