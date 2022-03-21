def getHigherAndLower(firstNumber, secondNumber, thirdNumber):
    if firstNumber < secondNumber:
        firstNumber, secondNumber = secondNumber, firstNumber

    if firstNumber < thirdNumber:
        firstNumber, thirdNumber = thirdNumber, firstNumber

    if secondNumber < thirdNumber:
        secondNumber, thirdNumber = thirdNumber, secondNumber

    return firstNumber, thirdNumber

print(getHigherAndLower(23, 43, 1))