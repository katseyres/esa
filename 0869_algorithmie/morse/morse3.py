

def tradmorse(dico):
    entree = input('Tapez votre phrase.').lower()
    phrase = ''
    for i in entree:
        if i in dico.keys():
            phrase += dico[i]
            phrase += " "
        else:
            print(i," n'a pas d'équivalence morse.")
            return False
    print(phrase)
    
    
while tradmorse(alphanum_mose) is False:
    tradmorse(alphanum_mose)