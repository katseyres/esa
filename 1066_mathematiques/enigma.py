import string

ALPHABET = list(string.ascii_uppercase)

AVAILABLE_ROTORS = [
    ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"],
    ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"],
    ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"],
    ["E", "S", "O", "V", "P", "Z", "J", "A", "Y", "Q", "U", "I", "R", "H", "X", "L", "N", "F", "T", "G", "K", "D", "C", "M", "W", "B"],
    ["V", "Z", "B", "R", "G", "I", "T", "Y", "U", "P", "S", "D", "N", "H", "L", "X", "A", "W", "M", "J", "Q", "O", "F", "E", "C", "K"]
]

REFLECTOR = ["Y", "R", "U", "H", "Q", "S", "L", "D", "P", "X", "N", "G", "O", "K", "M", "I", "E", "B", "F", "Z", "C", "W", "V", "J", "A", "T"]

def select_rotors(first:int, second:int, third:int):
    return [AVAILABLE_ROTORS[first], AVAILABLE_ROTORS[second], AVAILABLE_ROTORS[third]]

selected_rotors = select_rotors(0, 1, 2)

""" Il y a 5 rotors disponibles. Il faut en choisir 3.
    Chacun de ces rotors à une position initiale.
    Pour chaque lettre encodée, il faut déplacer un des rotors.
    Un rotor possède 26 éléments (pour l'alphabet).
    À chaque lettre écrite, au moins 1 rotor bouge d'un cran.
    - Le troisième rotor est celui qui bouge en premier. À la fin du tour le troisième revient à sa position initiale et le deuxième avance d'un cran.
    - Le deuxième rotor est celui qui bouge en deuxième. À la fin de 26 tours du premier, il avance d'un cran.
    - Le premier rotor est celui qui bouge en dernier. À la fin de 26 tours du deuxième, il avance d'un cran.

    Lorsque le premier rotor a terminé son cycle, il faut recommencer à 0.
"""

def get_reflected_letter(letter:str, rotor:list):
    return rotor[ALPHABET.index(letter)]

word = "GVUR"
new_word = ""
# print(get_reflected_letter("C", selected_rotors[0]))

# def encrypt():
for i in range(len(word)):
    print(word[i])
    letter = word[i]
    for j in range(len(selected_rotors)):
        letter = get_reflected_letter(letter, selected_rotors[j])
    new_word += letter
    
    print(f"alpha: {ALPHABET}")
    print(f"avail: {AVAILABLE_ROTORS[0]}")
    print(f"actua: {selected_rotors[0]}")
    print(f"lette: {letter}")
    
    last_element = selected_rotors[0][0]
    # rotor = rotor[1:]
    selected_rotors[0] = selected_rotors[0][1:]
    selected_rotors[0].append(last_element)
    # print(selected_rotors[0])
    
    
print(word, new_word)

available_rotor = AVAILABLE_ROTORS[0]
last_element = available_rotor[0]
available_rotor = available_rotor[1:]
available_rotor.append(last_element)

# print(AVAILABLE_ROTORS[0].index(available_rotor[0]))

# print(available_rotor)