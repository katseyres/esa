TABLEAU = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

def calculLignesColonnes(tableau:list):
  sommeColones = list((0 for i in tableau))
  sommeLignes = []

  for i,row in enumerate(tableau):
    sommeLignes.append(sum(row))


    for j,elem in enumerate(row):
      sommeColones[j] += elem

  return sommeLignes, sommeColones

print(calculLignesColonnes(TABLEAU))