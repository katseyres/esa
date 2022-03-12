def getInterval(firstNumber, secondNumber):   
    interval = []

    if firstNumber > secondNumber:
        firstNumber, secondNumber = secondNumber, firstNumber

    
    while firstNumber <= secondNumber:        
        interval.append(firstNumber)
        firstNumber += 1
    
    return interval

print(getInterval(23, 12))