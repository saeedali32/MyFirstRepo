secret_word = "Cow"
guess = " "
guess_count = 0 
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses): # while Guess is not secret word 
    if guess_count < guess_limit:
        guess = input("Enter guess: ") # Keep asking till above line is true 
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose")
else:
    print("You Win")

