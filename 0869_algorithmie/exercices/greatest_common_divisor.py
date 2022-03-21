def greatestCommonDivisor(firstNumber, secondNumber):
    pgcd = 0
    
    if firstNumber > secondNumber:
        pgcd = secondNumber
    else:
        pgcd = firstNumber

    while (pgcd > 0):
        if (firstNumber % pgcd == 0) and (secondNumber % pgcd == 0):
            break
        pgcd -= 1
    
    return pgcd

print(greatestCommonDivisor(30, 20))