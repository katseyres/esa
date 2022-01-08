import random
import json
import string

def fetch_data():
    """Fetch words from a json file and return the list."""

    with open("./database_hangman.json") as file:
        data  = json.load(file)    
    return data

def hangman_game():
    """
        #### Start the hangman game.
        You have 20 lifes. If you find the word before you consume all lifes, you win, otherwise you lose.
        The word that you have to find is an english word.
    """

    letters = string.ascii_lowercase
    words = fetch_data()
    word = list(random.choice(words))
    hiddenWord = list("*"*len(word))
    lifes = 20
    
    while lifes > 0:
        print("life(s): {}".format(lifes))
        letterSolution = input("Choose a letter: ").lower()

        # If you already have proposed this letter.
        if (letterSolution not in letters):
            print("Already provided")
        else:
            # If the word doesn't contain this letter.
            if (letterSolution not in word):
                letters = letters.replace(letterSolution, "")
                lifes -= 1
                print("{} not in the word {}, {}".format(letterSolution, "".join(hiddenWord), letters))
            else:
                # Find this letter in the word (maybe more than once) and replace "*" to this letter in the hidden word,
                for key,letter in enumerate(word):
                    if letter == letterSolution:
                        hiddenWord.pop(key)
                        hiddenWord.insert(key, letter)
                
                # Remove this letter from the alphabet.
                letters = letters.replace(letterSolution, "")

                # Check if the hidden word no longer contains any hidden letter.
                if not hiddenWord.__contains__("*"):
                    print("You found the word: %s" %''.join(hiddenWord))
                    return True
                
                print("{} in the word {}, {}".format(letterSolution, "".join(hiddenWord), letters))

hangman_game()