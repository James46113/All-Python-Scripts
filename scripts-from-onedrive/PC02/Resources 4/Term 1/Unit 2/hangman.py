def play_hangman(word):
    guessed_letters = []
    revealed_letters = []
    for index in range(len(word)):
        revealed_letters.append(False)
    lives_left = 10
    while lives_left > 0:
        revealed_string = ""
        for index in range(len(word)):
            revealed_string += (word[index] if revealed_letters[index] else "_") + " "
        print("Revealed Word: {}".format(revealed_string))
        if len(revealed_letters) == len([revealed for revealed in revealed_letters if revealed]):
            print("You have revealed all the letters!")
            print("You did so with {} lives remaining, good job".format(lives_left))
            return
        print("Guessed Letters: {}".format(", ".join(guessed_letters)))
        print("Lives Left: {}".format(lives_left))
        print("What is your next guess?")
        while True:
            guess = input("Letter: ").lower()
            if len(guess) > 1 or len(guess) == 0:
                print("Please enter a single letter next time")
            elif not guess.isalpha():
                print("Please enter only a letter (a - z) next time")
            elif guess in guessed_letters:
                print("You cannot make the same guess twice")
            break
        print("You chose {}".format(guess))
        guessed_letters.append(guess)
        found = False
        for index in range(len(word)):
            if word[index] == guess:
                found = True
                revealed_letters[index] = True
        if found:
            print("Good job! That letter was in the word")
        else:
            print("Unfortunately, that letter was not in the word")
            lives_left -= 1


def setup_hangman():
    print("----------HANGMAN----------")
    print("Please start by adding words to the Dictionary (leave the input blank to stop adding)")
    words = []
    while True:
        word = input("Word: ")
        if len(word) == 0:
            break
        words.append(word.lower())
    dictionary = Dictionary(words)
    random_choice = False
    while True:
        choice = input("Would you like a random word or to choose a word (1 or 2): ")
        if choice == "1":
            random_choice = True
            break
        elif choice == "2":
            break
        else:
            print("Please choose correctly...")
    if random_choice:
        chosen_word = dictionary.get_random_word()
    else:
        dictionary.output()
        while True:
            try:
                choice = int(input("Please choose the word (by its index): "))
                chosen_word = dictionary.get_word(choice)
                break
            except ValueError:
                print("Please enter a valid integer")
            except IndexError:
                print("Please enter a valid index between 0 and {}".format(dictionary.get_length()))
    play_hangman(chosen_word)


if __name__ == "__main__":
    setup_hangman()
