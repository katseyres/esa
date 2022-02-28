dictionnary = {
    "bonjour": "hello",
    "s'il-vous-plait": "please",
    "manger": "eat",
    "voiture": "car"
}

def inversion_keys_values(arg:dict):
    output = dict()

    for key in arg:
        output[arg[key]] = key
    
    return output

print(inversion_keys_values(dictionnary))