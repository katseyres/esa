CSV_PATH = "./morse_dictionary.csv"
morse = {}

def read_csv(file:str):
    output = {}
    
    with open(file, "r") as f:
        data = f.read().split("\n")
        for letter in data:
            output[letter.split(",")[0]] = letter.split(",")[1]
    
    return output

def show_morse_table(haystack:dict):
    output = ""

    for key,value in haystack.items():
        output += f"{key} : {value}\n"
    
    return output

def is_morse_code(arg:str):
    filter = arg.replace(" ", "").replace("─", "").replace("·", "")    
    return not len(filter) > 0

def morse_to_alpha(needle:str, haystack:dict):
    if needle is " ":
        return needle
    if is_morse_code(needle) is False:
        return False
    if list(haystack.values()).__contains__(needle) is False:
        return False

    return list(haystack.keys())[list(haystack.values()).index(needle)]

def alpha_to_morse(needle:str, haystack:dict):
    if needle is " ":
        return needle
    if list(haystack.keys()).__contains__(needle.upper()) is False:
        return False
    
    return haystack[needle.upper()]

if __name__ == '__main__':
    CODE = "·─ ─···   "

    morse =  read_csv(CSV_PATH)
    # print(show_morse_table(morse))
    # print(is_morse_code(CODE))
    # print(morse_to_alpha("-•-", morse))
    # print(alpha_to_morse("-", morse))


    while True:
        response = input("\nMenu\n\
  1. Show Morse table\n\
  2. Morse -> Alphabet\n\
  3. Alphabet -> Morse\n\
  4. Exit\n\n\
Choice: ")

        try:
            int(response)
        except:
            print("\n[INFO] You must enter an integer.")
            continue
        
        choice = int(response)

        if (choice == 1):
            print("\n─── MORSE TABLE ───\n")
            print(show_morse_table(morse))
            print("─" * 19)
        elif (choice == 2):
            print("\n─── MORSE → ALPHA ───\n")
            response = input("What's your sentence ?\n→  ")
            print("")
            translation = ""
            for morse_char in response.split(" "):
                if morse_char is "":
                    translation += " "
                else:
                    letter_translated = morse_to_alpha(morse_char, morse)
                    if letter_translated is False:
                        translation += "\uFFFD"
                        print(f"[INFO] The character '{morse_char}' doesn't exist in morse code.")
                    else:
                        translation += letter_translated

            print(f"[TRANSLATION]\nMorse: {response}\nAlpha: {translation}\n")
            print("─" * 21)
        elif (choice == 3):
            print("\n─── ALPHA → MORSE ───\n")
            response = input("What's your sentence ?\n→  ")
            print("")
            translation = ""
            for letter in list(response):
                translated = alpha_to_morse(letter, morse)
                if translated is False:
                    translation += "\uFFFD"
                    print(f"[INFO] The character '{letter}' doesn't exist in alpha code.")
                else:
                    translation += translated + " "
            print(f"[TRANSLATION]\n {translation}")
        elif (choice == 4):
            break
        else:
            print("\n[INFO] choisir une des quatres actions disponibles (1, 2, 3 ou 4)")