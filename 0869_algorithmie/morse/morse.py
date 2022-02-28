import morse_talk
import string

def show_morse_table():
    print("\n-- ALPHABET MORSE --\n")

    for element in string.ascii_lowercase:
        print(f"{element} : {morse_talk.encode(element)}")

def morse_to_alpha():
    print("\n-- CONVERSION MORSE -> ALPHABET --\n")
    morse = input("Chaine morse : ")

    filterDashes = morse.replace("-", "")
    filterDots = filterDashes.replace(".", "")

    if len(filterDots) > 0:
        print("\n[INFO] morse ne peut que contenir '-' and '.'")
        return

    try:
        print(f"Conversion : {morse_talk.decode(morse)}")
    except:
        print(f"\n[ERROR] impossible de convertir la chaine '{morse}'")

def alpha_to_morse():
    print("\n-- CONVERSION ALPHABET -> MORSE --")
    alpha = input("Chaine alpha : ")

    try:
        print(f"Conversion : {morse_talk.encode(alpha)}")
    except:
        print(f"\n[ERROR] impossible de convertir la chaine '{alpha}'")


if __name__ == '__main__':
    while True:
        response = input("\nMenu\n\
  1. Afficher l'alphabet Morse\n\
  2. Conversion Morse -> alphabet\n\
  3. Conversion alphabet -> Morse\n\
  4. Quitter\n\n\
Choix: ")

        try:
            int(response)
        except:
            print("\n[INFO] Le choix doit etre un entier")
            continue
        
        choice = int(response)

        if (choice == 1):
            show_morse_table()
        elif (choice == 2):
            morse_to_alpha()
        elif (choice == 3):
            alpha_to_morse()
        elif (choice == 4):
            break
        else:
            print("\n[INFO] choisir une des quatres actions disponibles (1, 2, 3 ou 4)")
            continue