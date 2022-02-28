import string


def tuto_set():
  my_set = {1, 2, 3}
  my_set2 = set((3, 4, 5))
  my_set3 = set([5, 6, 7])
  
  print(my_set)
  print(my_set2)
  print(my_set3)

  # Intersection.
  print(my_set & my_set2)
  # Union.
  print(my_set | my_set2)
  # Equality. 
  print(my_set == my_set2)
  # Symmetric difference.
  print(my_set ^ my_set2)

  my_set.add(0)
  print(my_set)
  my_set.add(3)

# Exercice 01
# Écrire un programme qui lit une phrase et qui affiche par ordre alphabétique, les lettres (minuscules) que
# la phrase ne contient pas. Les lettres majuscules utilisées dans la phrase compteront comme minuscules.

def getLetterNotUsed(sentence:str):
  alpha = string.ascii_lowercase

  return "".join(sorted(list(set(alpha) ^ set(sentence.lower()) & set(alpha))))
  

print(getLetterNotUsed("HelloaWorld!"))

# Exercice 02
# Écrire un programme définissant deux types d'ensembles composés, d'une part des consonnes et d'autre part
# des voyelles. Après lecture d'une phrases, afficher le nombre de consonnes et de voyelles utilisées et affichez-les.

def getUserLetters(firstSet:set, secondSet:set):
  alpha = string.ascii_letters

  return (firstSet | secondSet) & set(alpha);

print(getUserLetters(set(("!", "b", "e")), set(("x", "y", "z"))))
