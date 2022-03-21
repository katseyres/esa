def getFactorialAddition(number):
    result = 0

    while number > 0:
        result += number
        number -= 1
    return result


print(getFactorialAddition(8))