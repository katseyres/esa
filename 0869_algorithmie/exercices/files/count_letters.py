import os
import string

PATH = "./data.txt"
alpha_lowercase_counter = {}
alpha_uppercase_counter = {}
digit_counter = {}
special_counter = {}

class FileService:

    def read(path:str):
        with open(path, "r") as file:
            return file.read()

    def add(path:str, data:str):
        with open(path, "a") as file:
            file.write(data)

    def write(path:str, data:str):
        with open(path, "w") as file:
            file.write(data)

    def clear(path:str):
        with open(path, "w") as file:
            file.write("")
        
    def create(path:str):
        file = open(path, "x")
        file.close()

    def remove(path:str):
        os.remove(path)
    
    def count_letter(path:str, letter:str):
        return FileService.read(path).count(letter)

if "__main__" == __name__:
    file = FileService.read(PATH)

    for letter in string.ascii_lowercase:
        alpha_lowercase_counter[letter] = file.count(letter)
        file = file.replace(letter, "")

    
    for letter in string.ascii_uppercase:
        alpha_uppercase_counter[letter] = file.count(letter)
        file = file.replace(letter, "")
    
    for digit in string.digits:
        digit_counter[digit] = file.count(digit)
        file = file.replace(digit, "")
    
    file = file.replace(" ", "")

    for char in file:
        special_counter[char] = char.count(file)
        file = file.replace(char, "")

    print(alpha_lowercase_counter)
    print(alpha_uppercase_counter)
    print(digit_counter)
    print(special_counter)