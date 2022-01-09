from checks import checkPostCode, checkName, checkPassword, checkUsername, checkEmail

"""
katseyres
Admin123456_
Maximilien
Denis
5170
den@den.fr

pabloooo
PaBloooo123__
Pablo
Escobar
3298
pab@pab.pa
"""

username = ""
password = ""
firstname = ""
lastname = ""
postCode = 0
email = ""

dataRightEncoded = False

username = input("Select an username: ")
password = input("Select a password: ")
firstname = input("Select a firstname: ")
lastname = input("Select a lastname: ")
postCode = int(input("Select a post code: "))
email = input("Select an email: ")

def displayUserInfo(password, firstname, lastname, email, postCode, username):
    print(
        f"\n\
    USER INFORMATION\n\
    | Username: {username}\n\
    | Password: {'*' * len(password)}\n\
    | Firstname: {firstname}\n\
    | Lastname: {lastname}\n\
    | Post code: {postCode}\n\
    | Email: {email}"
    )

def allTests(password, firstname, lastname, email, postCode, username):
    if checkPassword(password) is False:
        print(f"\n/!\\ {checkPassword.__doc__}")
        password = input(f"--> Please select another password: ")
        print(password)
        return False
    if checkName(firstname, lastname) is False:
        print(f"\n/!\\ {checkName.__doc__}")
        firstname = input("--> Please select another firstname: ")
        lastname = input("--> Please select another lastname: ")
        return False
    if checkEmail(email) is False:
        print(f"\n/!\\ {checkEmail.__doc__}")
        email = input("--> Please select another email: ")
        return False
    if checkPostCode(postCode) is False:
        print(f"\n/!\\ {checkPostCode.__doc__}")
        postCode = input("--> Please select another post code: ")
        return False
    if checkUsername(username) is False:
        print(f"\n/!\\ {checkUsername.__doc__}")
        username = input("--> Please select another username: ")
        return False
    
    return True

while dataRightEncoded is False:
    dataRightEncoded = allTests(password, firstname, lastname, email, postCode, username)
    
displayUserInfo(password, firstname, lastname, email, postCode, username)

response = input("\nDo you want add a second user? (y/n) ").lower()

if response == "y":
    secondUsername = input("Select an username: ")
    password = input("Select a password: ")
    firstname = input("Select a firstname: ")
    lastname = input("Select a lastname: ")
    postCode = int(input("Select a post code: "))
    email = input("Select an email: ")

    while secondUsername == username:
        secondUsername = input("/!\ Usersname already taken, please select another one: ")

    dataRightEncoded = False
   
    while dataRightEncoded is False:
        dataRightEncoded = allTests(password, firstname, lastname, email, postCode, username)
        
    displayUserInfo(password, firstname, lastname, email, postCode, secondUsername)