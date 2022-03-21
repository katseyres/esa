alphanum_mose = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "à": ".--.-",
    "ç": "-.-..",
    "è": ".-..-",
    "é": "..-..",
    ".": ".-.-.-",
    "?": "..--..",
    "!": "-.-.--",
    "@": ".--.-.",
    ",": "--..--",
    "'": ".----.",
    " ": "/",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "+": ".-.-.",
    "-": "-....-",
    "=": "-...-",
    "_": "..--.-",
    "$": "...-..-",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-.....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

def character_in_dictionary(letter: str, dictionary: dict):
    """
    Check if the letter is in the dictionary.
    """

    keys = list(dictionary.keys())
    return keys.__contains__(letter)

def alpha_to_morse(sentence: str, dictionary: dict):
    """
    Convert an alphabetic sentence into a morse sentence.
    """

    output = ""
    for letter in sentence:
        if character_in_dictionary(letter, dictionary) is False:
            print(f"The letter {letter} isn't in the dictionary")
            return False
        output += dictionary[letter] + " "
    return output

if __name__ == '__main__':
    sentence_to_translate = input("May you enter your sentence: ").lower()
    translate = alpha_to_morse(sentence_to_translate, alphanum_mose)
    if translate is False:
        print("Wrong sentence")
    else:
        print(translate)
