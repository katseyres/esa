import string
import re


def checkPostCode(postCode:int) -> bool:
    """Check if the post code contains exaclty 4 digits."""
    return (type(postCode) == int and len(str(postCode)) == 4)

def checkEmail(email:str) -> bool:
    """The email must match with the pattern xxx@xxx.xx and must only contain alpha lowercase, integers or "." and "-"."""
    pattern = r"^[a-z0-9\.\-]{3}@[a-z0-9\.\-]{3}\.[a-z0-9\.\-]{2}$"
    output = re.match(pattern, email)

    return output is not None

def checkPassword(password:str) -> bool:
    """The password must contain at least
        - 10 characters.
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

    # print(hasAlphaLower)
    # print(hasAlphaUpper)
    # print(hasDigit)
    # print(hasSpecialChar)
    
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


def checkUsername(username:str) -> bool:
    """The username must contain only lowercase alpha or digits."""
    pattern = r"^[a-z0-9]+$"
    return re.match(pattern, username) is not None


def checkName(firstName:str, lastName:str) -> bool:
    """Firstname and lastname must contain only letters or "-"."""

    if firstName == lastName:
        return False

    chars = string.ascii_letters + "-"
        
    for letter in firstName:
        if chars.__contains__(letter) is False:
            return False

    for letter in lastName:
        if chars.__contains__(letter) is False:
            return False
    
    return True