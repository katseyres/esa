import string

# Exercice 02
# Écrire un programme définissant deux types d'ensembles composés, d'une part des consonnes et d'autre part
# des voyelles. Après lecture d'une phrases, afficher le nombre de consonnes et de voyelles utilisées et affichez-les.

def getUserLetters(firstSet:set, secondSet:set):
  alpha = string.ascii_letters

  return (firstSet | secondSet) & set(alpha);

print(getUserLetters(set(("!", "b", "e")), set(("x", "y", "z"))))