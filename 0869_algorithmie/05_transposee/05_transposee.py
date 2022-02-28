import copy

MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def isMatrix(arg):
    if type(arg) != list:
        return False
    elif len(arg) == 0:
        return False
    
    return bool(type(arg[0]) == list) 

def isSquareMatrix(matrix:list):
    return len(matrix) == len(matrix[0])

def cofactors(matrix:list):
    if isMatrix(matrix) is False:
        return False
    elif isSquareMatrix(matrix) is False:
        return False
    
    matrixCopy = copy.deepcopy(matrix)

    for i,row in enumerate(matrix):
        # print(matrixCopy[i])
        for j,elem in enumerate(row):
            del matrixCopy[i][j]
            pass
        del matrixCopy[i]
        print(matrixCopy)
    
cofactors(MATRIX)