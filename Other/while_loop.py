correct = "IndyPy"
tries = 0

keep_going = True
while(keep_going):
    tries = tries + 1
    print("try # ", tries)

    guess = input("What is the password? ")
    if guess == correct:
        print("Thats correct! Here's the treasure")
        keep_going = False

    elif tries >= 3:
        print("Too many wrong tries, Launching the missiles")
        keep_going = False 