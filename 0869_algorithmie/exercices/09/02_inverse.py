def inverse(tableau:list):
    return list(tableau.__reversed__())

TABLEAU = [1, 2, 4, 5, 6, 9]

print(inverse(TABLEAU))