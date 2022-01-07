import random
import json
import string

def fetch_data():
    with open("./database_hangman.json") as file:
        data  = json.load(file)    
    return data

def hangman_game():
    letters = string.ascii_lowercase
    words = fetch_data()
    word = list(random.choice(words))
    hiddenWord = list("*"*len(word))
    lifes = 20

    print(word)
    
    while lifes > 0:
        print("life(s): {}".format(lifes))

        letterSolution = input("Choose a letter: ").lower()
        if (letterSolution not in letters):
            print("Already provided")
        else:
            if (letterSolution not in word):
                letters = letters.replace(letterSolution, "")
                lifes -= 1
                print("{} not in the word {}, {}".format(letterSolution, "".join(hiddenWord), letters))
            else:
                for key,letter in enumerate(word):
                    if letter == letterSolution:
                        hiddenWord.pop(key)
                        hiddenWord.insert(key, letter)

                letters = letters.replace(letterSolution, "")
                if not hiddenWord.__contains__("*"):
                    print("You found the word: %s" %''.join(hiddenWord))
                    return True
                
                print("{} in the word {}, {}".format(letterSolution, "".join(hiddenWord), letters))

hangman_game()