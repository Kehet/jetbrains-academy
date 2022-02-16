import random

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']
word = ""
status = ""

def reveal_letter(_guess):
    global status

    out = ""
    for index, letter in enumerate(word):
        if letter == _guess:
            out = out + _guess
        else:
            out = out + status[index]
    status = out


def main_loop():
    global word
    global status

    word = random.choice(words)
    status = "-" * len(word)
    guessed_letters = ""
    guesses = 0
    while guesses < 8:
        print()
        print(status)
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print("You should input a single letter")
            continue

        if guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a lowercase English letter")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter")
        elif guess in word:
            reveal_letter(guess)
            guessed_letters = guessed_letters + guess
        else:
            guesses = guesses + 1
            guessed_letters = guessed_letters + guess
            print("That letter doesn't appear in the word")

        if status == word:
            break

    if guesses < 8:
        print()
        print(status)
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")


while True:
    command = input('Type "play" to play the game, "exit" to quit: ')

    if command == "play":
        main_loop()
    elif command == "exit":
        break
