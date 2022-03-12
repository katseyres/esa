import string

# Exercice 01
# Écrire un programme qui lit une phrase et qui affiche par ordre alphabétique, les lettres (minuscules) que
# la phrase ne contient pas. Les lettres majuscules utilisées dans la phrase compteront comme minuscules.

def getLetterNotUsed(sentence:str):
  alpha = string.ascii_lowercase

  return "".join(sorted(list(set(alpha) ^ set(sentence.lower()) & set(alpha))))
  

print(getLetterNotUsed("HelloaWorld!"))
