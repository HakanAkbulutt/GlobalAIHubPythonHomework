# Hangman Game

name = input("Please enter your name: ")
name = name.upper()
print("WELCOME " +name+ "." + " TIME TO PLAY HANGMAN!")

word = "python"
guesses = []
attempts = 10

while attempts > 0:
    counter = 0
    guess = input("Guess a char: ")
    guesses.append(guess)

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("#")
            counter = counter + 1

    if guess not in word:
        attempts = attempts - 1
        print("False char")
        print("Attempts Remaining: " + str(attempts) )

    if attempts == 0:
        print("You lost the game...")

    if counter == 0:
        print("\nCongratulations " + name + "!" + " You won the game.")
        print("\nWord: " + word)

        break