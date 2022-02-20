def view_nombres(nombre_max):
    sortie = ""
    index = 1

    if (nombre_max > 9 or nombre_max < 1):
        return "Le parametre doit etre compris entre 1 et 9."
    
    while index < nombre_max:
        ligne = (nombre_max - index) * " " + index * 2 * str(index)
        sortie += f"{ligne}\n"
        index += 1
    
    while index > 0:
        ligne = (nombre_max - index) * " " + index * 2 * str(index)
        sortie += f"{ligne}\n"
        index -= 1
    
    return sortie


for i in range(10):
    print(view_nombres(i))