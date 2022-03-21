dico_etudiant = []
auto_increment_id = 1000

def check_name(arg:str):
    if (len(arg) == 0):
        print("[ERREUR] champ vide")
        return False
    
    if (type(arg) != str):
        print("[ERREUR] chaine de caractères requis")
        return False
    
    return True

def check_age(age:int):    
    if ((0 < age < 150) is False):
        print("L'âge doit être compris entre 0 et 150 ans exclus")
        return False
    
    return True

def show_students():
    print("\n-- ETUDIANT(S) --")

    if (len(dico_etudiant) == 0):
        print("Aucun étudiant")
        return

    for student in dico_etudiant:
        print(f"\n  Id           : {student['id']}\n\
  Prénom       : {student['firstname']}\n\
  Nom          : {student['lastname']}\n\
  Age          : {student['age']}")

def add_student(auto_increment_id):
    print("\n-- NOUVEAU ETUDIANT --")
    firstname = input("|-> Prénom : ")
    lastname = input("|-> Nom : ")
    age = input("|-> Age : ")

    try:
        age = int(age)
    except:
        print("\n[ERREUR] l'age doit etre un entier.")
        return

    if (check_name(firstname) is False):
        print("[ERREUR] prénom incorrect")
        return False
    
    if (check_name(lastname) is False):
        print("[ERREUR] nom incorrect")
        return False

    if (check_age(age) is False):
        print("[ERREUR] age incorrect")
        return False

    dico_etudiant.append({
        "id": auto_increment_id,
        "firstname":  firstname,
        "lastname": lastname,
        "age": age,
    })

    print("Étudiant ajouté")
    return auto_increment_id + 1

def remove_student():
    print("\n-- SUPPRESSION --")

    for student in dico_etudiant:
        print(f"{student['id']} : {student['firstname']} {student['lastname']}")

    print("\n(NB : entrer 'Q' pour annuler)")

    response = input("\nRetirer quel étudiant [id] : ")
    
    if (response == 'Q'):
        return True
    
    try:
        print(int(response))
    except:
        print("\n[ERREUR] l'identifiant doit etre un entier")
        return

    response = int(response)

    index = -1

    for student in dico_etudiant:
        if (student["id"] == response):
            index = dico_etudiant.index(student)
            break
    
    if index == -1:
        print("\n[INFO] aucun etudiant avec cet identifiant")
        return

    dico_etudiant.pop(index)
    print("\n[INFO] etudiant supprime")

def edit_student():
    for student in dico_etudiant:
        print(f"{student['id']} : {student['firstname']}")

    print("NB : entrer 'Q' pour annuler")
    id = input("\nEditer quel etudiant [id] : ")

    try:
        id = int(id)
    except:
        print("\n[ERREUR] l'identifiant doir etre un entier")
        return
    
    found = False

    for student in dico_etudiant:
        if student["id"] == id:
            found = True
            break
    
    if found is False:
        print("\n[INFO] aucun etudiant avec cet identifiant")
        return

    firstname = input(f"\n|-> Prénom ({student['firstname']}) : ")
    lastname = input(f"|-> Nom ({student['lastname']}): ")
    age = input(f"|-> Age ({student['age']}): ")

    if (check_name(firstname) is False):
        print("[ERREUR] prénom incorrect")
        return False
    
    if (check_name(lastname) is False):
        print("[ERREUR] nom incorrect")
        return False

    if (check_age(int(age)) is False):
        print("[ERREUR] age incorrect")
        return False
    
    for student in dico_etudiant:
        if (student['id'] == id):
            student['firstname'] = firstname
            student['lastname'] = lastname
            student['age'] = age    

if __name__ == '__main__':
    while (True):
        choice = input("\nMenu\n\
  1. Montrer la liste d'étudiants\n\
  2. Ajouter un étudiant\n\
  3. Supprimer un étudiant\n\
  4. Mettre à jour un étudiant\n\
  5. Quitter le programme\n\
\nChoix : ")

        try:
            choice = int(choice)
        except:
            print("\n[ERROR] Mauvais format")
            continue
                    
        if (choice == 1):
            show_students()
        elif (choice == 2):
            auto_increment_id = add_student(auto_increment_id)
        elif (choice == 3):
            remove_student()
        elif(choice == 4):
            edit_student()
        elif (choice == 5):
            break
        else:
            print("\n[INFO] Choisir un des chiffres proposés.")
