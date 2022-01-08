import string
import re
from sys import hash_info

def checkName(firstName:str, lastName:str) -> bool:
    """CHeck if parameters only to contain letters or "-"."""

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

    return firstNameChecked and lastNameChecked

def checkPostCode(postCode:int) -> bool:
    """Check if the post code contains exaclty 4 digits."""
    return (type(postCode) == int and len(str(postCode)) == 4)

def checkEmail(email:str) -> bool:
    """Check if the email matches with the pattern xxx@xxx.xx."""
    pattern = r"^[a-z0-9\.\-]{3}@[a-z0-9\.\-]{3}\.[a-z0-9\.\-]{2}$"
    output = re.match(pattern, email)
    print('Email match: {0}'.format(output))

    return output is not None

def checkUsername(username:str) -> bool:
    """Check if the username only contains lowercase alpha or digits."""
    pattern = r"^[a-z0-9]+$"
    return re.match(pattern, username) is not None

def checkPassword(password:str) -> bool:
    """Check if the password contains at least
        - One lowercase alpha.
        - One uppercase alpha.
        - One digit.
        - One special character.  
    """
    alphaLowerPattern = r"[a-z]"
    alphaUpperPattern = r"[A-Z]"
    digitPattern = r"[0-9]"
    specialCharPattern = r"[^a-z^A-Z^0-9]"

    hasAlphaLower = re.search(alphaLowerPattern, password)
    hasAlphaUpper = re.search(alphaUpperPattern, password)
    hasDigit =  re.search(digitPattern, password)
    hasSpecialChar =  re.search(specialCharPattern, password)

    print(hasAlphaLower)
    print(hasAlphaUpper)
    print(hasDigit)
    print(hasSpecialChar)
    
    if (len(password) < 10):
        return False
    elif (hasAlphaUpper is None):
        return False
    elif (hasAlphaUpper is None):
        return False
    elif (hasDigit is None):
        return False
    elif (hasSpecialChar is None):
        return False

    return True


print(checkName("Maximilien", "Denis"))
print(checkPostCode(2333))
print(checkEmail("eee@zzz.zz"))
print(checkUsername("eeduzfiu1"))
print(checkPassword("ozeEi8cb_rfy"))
