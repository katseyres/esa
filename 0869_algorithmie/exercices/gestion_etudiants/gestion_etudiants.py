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

def check_information(fields):
    if len(fields) != 3:
        return False

    if type(fields[0]) != str or type(fields[1]) != str:
        return False

    if len(fields[0]) <= 0 or len(fields[1]) <= 0:
        return False

    if type(fields[2]) != int:
        return False

    if fields[2] <= 0 or fields[2] > 150:
        return False
    
    return True

def add_student(auto_increment_id, fields:list):
    if type(auto_increment_id) != int:
        return None
    
    if auto_increment_id < 0:
        return None
    
    if check_information(fields) is False:
        return None
    
    student = { "id": auto_increment_id }      
    student["firstname"] = fields[0]
    student["lastname"] = fields[1]
    student["age"] = int(fields[2])

    return student

def is_student(student:dict):
    if type(student['id']) != int:
        return False
    
    if student['id'] < 0:
        return False
    
    student.pop('id')

    if check_information(list(student.values)) is False:
        return False
    
    return True

def remove_student(id, students:list):
    if type(id) != int or type(students) != list:
        return False

    for s in students:
        if is_student is False:
            return False
    
    index = -1

    for s in students:
        if (s["id"] == id):
            index = students.index(student)
            students.pop(index)
            return students
            
    return False
    

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
            print("\n-- CREATION ETUDIANT --")
            response = input('<firstname> <lastname> <age>\n >> ')

            if (len(response) != 3):
                print("wrong cmdline")
                continue

            student = add_student(auto_increment_id, response)
            if student:
                students.append(student)
                auto_increment_id += 1
        elif choice == 3:
            print("\n-- SUPPRESSION --")
            show_students()
            print("\n(NB : entrer 'Q' pour annuler)")
            response = input("\nRetirer quel etudiant [id] : ")
            students = remove_student(response, students)
        elif choice == 4:
            students = edit_student(dico_etudiant, fields)
        elif choice == 5:
            fields = add_field(fields)
        elif choice == 6:
            fields = remove_field(fields)
        elif choice == 7:
            break
        else:
            print("\n[INFO] Choisir un des chiffres proposes.")
