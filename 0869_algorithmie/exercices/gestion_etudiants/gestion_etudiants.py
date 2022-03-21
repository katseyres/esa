dico_etudiant = [
    {
        "id": 998,
        "firstname": "Maximilien",
        "lastname": "Denis",
        "age": 23
    },
    {
        "id": 999,
        "firstname": "Jeanne",
        "lastname": "Petit",
        "age": 20
    }
]

fields = ["firstname", "lastname", "age"]
auto_increment_id = 1000

def check_name(arg:str):
    if (len(arg) == 0):
        print("[ERREUR] champ vide")
        return False
    
    if (type(arg) != str):
        print("[ERREUR] chaine de caracteres requis")
        return False
    
    return True

def check_age(age:int):    
    if ((0 < age < 150) is False):
        print("L'age doit etre compris entre 0 et 150 ans exclus")
        return False
    
    return True

def show_students():
    print("\n-- ETUDIANT(S) --")

    if (len(dico_etudiant) == 0):
        print("Aucun etudiant")
        return

    for student in dico_etudiant:
        print(f"\nEtudiant {student['id']}")
        for field in fields:
            try:
                print(f"- {field} : {student[field]}")
            except:
                print(f"- {field} : null")

def add_student(auto_increment_id, fields):
    print("\n-- CREATION ETUDIANT --")

    new_student = {
        "id": auto_increment_id
    }

    for field in fields:
        response = input(f"|-> {field} : ")        
        new_student[field] = response


    # try:
    #     age = int(age)
    # except:
    #     print("\n[ERREUR] l'age doit etre un entier.")
    #     return

    # if (check_name(firstname) is False):
    #     print("[ERREUR] prenom incorrect")
    #     return False
    
    # if (check_name(lastname) is False):
    #     print("[ERREUR] nom incorrect")
    #     return False

    # if (check_age(age) is False):
    #     print("[ERREUR] age incorrect")
    #     return False

    dico_etudiant.append(new_student)

    print("Etudiant ajoute")
    return auto_increment_id + 1

def remove_student():
    print("\n-- SUPPRESSION --")

    show_students()

    print("\n(NB : entrer 'Q' pour annuler)")

    response = input("\nRetirer quel etudiant [id] : ")
    
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

def add_field(fields:list) -> list:
    print("\n--- AJOUTER UN CHAMP ---\n")
    print(f"Champs actuels : {fields}")

    response = input("Ecrire le nom du champ a ajouter : ")
    confirm = input(f"Confirmer l'ajout du champ {response} (y/n) : ")

    if confirm.lower() == "y":
        fields.append(response)
    elif confirm.lower() != "n":
        print("You must enter 'y' or 'n'.")
    
    return fields

def remove_field(fields:list) -> list:
    if len(fields) <  2:
        print("Il faut avoir au moins un champ existant.")
        return fields

    print("\n--- RETIRER UN CHAMP ---")
    print(f"Champs actuels")
    for index,field in enumerate(fields):
        print(f"|-> {index} : {field}")
        
    response = input("Retirer quel champ (id) : ")

    try:
        response = int(response)
    except:
        print("La reponse doit etre un nombre entier.")
        return fields

    confirm = input("Confirmer la suppresion (y/n) : ")

    if confirm.lower() == "y":
        print(response)
        print(fields)
        fields.pop(int(response))
    elif confirm.lower() != "n":
        print("Vous devez entrer 'y' ou 'n'.")
    
    return fields

def edit_student(students, fields) -> list: 
    for student in students:
        print(f"| Etudiant {student['id']}")

    print("NB : entrer 'Q' pour annuler")
    id = input("\nEditer quel etudiant [id] : ")

    try:
        id = int(id)
    except:
        print("\n[ERREUR] l'identifiant doir etre un entier")
        return
    
    found = False
    edit_student = {}

    for student in students:
        if student["id"] == id:
            found = True
            edit_student = student
            break
        
    if found is False:
        print("\n[INFO] aucun etudiant avec cet identifiant")
        return
    
    for field in fields:
        edit_student[field] = input(f"|-> {field} : ")
    
    return students

    # firstname = input(f"\n|-> Prenom ({student['firstname']}) : ")
    # lastname = input(f"|-> Nom ({student['lastname']}): ")
    # age = input(f"|-> Age ({student['age']}): ")

    # if (check_name(firstname) is False):
    #     print("[ERREUR] prenom incorrect")
    #     return False
    
    # if (check_name(lastname) is False):
    #     print("[ERREUR] nom incorrect")
    #     return False

    # if (check_age(int(age)) is False):
    #     print("[ERREUR] age incorrect")
    #     return False
    
    # for student in dico_etudiant:
    #     if (student['id'] == id):
    #         student['firstname'] = firstname
    #         student['lastname'] = lastname
    #         student['age'] = age    

if __name__ == '__main__':
    my_list = ["a", "b", "c"]
    my_list.pop(0)
    print(my_list)


    while (True):
        choice = input("\nMenu\n\
  1. Montrer la liste d'etudiants\n\
  2. Ajouter un etudiant\n\
  3. Supprimer un etudiant\n\
  4. Mettre a jour un etudiant\n\
  5. Ajouter un champ\n\
  6. Retirer un champ\n\
  7. Quitter le programme\n\
\nChoix : ")

        try:
            choice = int(choice)
        except:
            print("\n[ERROR] Mauvais format")
            continue
                    
        if choice == 1:
            show_students()
        elif choice == 2:
            auto_increment_id = add_student(auto_increment_id, fields)
        elif choice == 3:
            remove_student()
        elif choice == 4:
            dico_etudiants = edit_student(dico_etudiant, fields)
        elif choice == 5:
            fields = add_field(fields)
        elif choice == 6:
            fields = remove_field(fields)
        elif choice == 7:
            break
        else:
            print("\n[INFO] Choisir un des chiffres proposes.")
