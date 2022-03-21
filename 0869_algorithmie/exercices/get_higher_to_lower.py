def getHigherToLower(firstNumber, secondNumber):
    if firstNumber < secondNumber:
        return secondNumber, firstNumber
    return firstNumber, secondNumber

print(getHigherToLower(3, 12))