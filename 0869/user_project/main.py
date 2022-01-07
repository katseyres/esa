import string
import re
from sys import hash_info

def checkName(firstName:str, lastName:str) -> bool:
    chars = string.ascii_letters + "-"

    firstNameChecked = True
    lastNameChecked = True
        
    for letter in firstName:
        if chars.__contains__(letter) is False:
            firstNameChecked = False
            break

    for letter in lastName:
        if chars.__contains__(letter) is False:
            lastNameChecked = False

    return firstNameChecked and lastNameChecked, firstName, lastName

print(checkName("Maximilien", "Denis"))

def checkPostCode(postCode:int) -> bool:
    return (type(postCode) == int and len(str(postCode)) == 4), postCode

print(checkPostCode(2333))

def checkEmail(email:str) -> bool:
    pattern = r"^[a-z0-9\.\-]{3}@[a-z0-9\.\-]{3}\.[a-z0-9\.\-]{2}$"
    output = re.match(pattern, email)

    return output is not None, output.group()

print(checkEmail("eee@zzz.zz"))

def checkUsername(username:str) -> bool:
    pattern = r"^[a-z0-9]+$"
    return re.match(pattern, username) is not None, re.match(pattern, username).group()

print(checkUsername("eeduzfiu1"))

def checkPassword(password:str) -> bool:
    alphaLowerPattern = r"[a-z]"
    alphaUpperPattern = r"[A-Z]"
    digitPattern = r"[0-9]"
    specialCharPattern = r"[^a-z^A-Z^0-9]"

    hasAlphaLower = re.search(alphaLowerPattern, password)
    hasAlphaUpper = re.search(alphaUpperPattern, password)
    hasDigit =  re.search(digitPattern, password)
    hasSpecialChar =  re.search(specialCharPattern, password)
    
    if (len(password) < 10):
        return False
    elif (re.search(alphaLowerPattern, password) is None):
        return False
    elif (re.search(alphaUpperPattern, password) is None):
        return False
    elif (re.search(digitPattern, password) is None):
        return False
    elif (re.search(specialCharPattern, password) is None):
        return False

    return True, (hasAlphaLower.group(), hasAlphaUpper.group(), hasDigit.group(), hasSpecialChar.group())

print(checkPassword("ozeEi8cb_rfy"))
