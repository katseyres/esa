import requests
import json
import time
import random

# maximilien informaticien 10 300 230 12 405 30 0.954 300 0 30

champions = [
    # {
    #     "name": "ashe",
    #     "class": "shooter",
    #     "hp": 570,
    #     "hp_regen": 3.5,
    #     "mana": 280,
    #     "mana_regen": 6.972,
    #     "range": 600,
    #     "attack_damage": 61,
    #     "attack_speed": 0.658,
    #     "armor": 26,
    #     "magic_resist": 30,
    #     "movement_speed": 325 
    # },
    # {
    #     "name": "vel'koz",
    #     "class": "magician",
    #     "hp": 520,
    #     "hp_regen": 5.5,
    #     "mana": 469,
    #     "mana_regen": 0.8,
    #     "range": 425,
    #     "attack_damage": 54.9379,
    #     "attack_speed": 0.625,
    #     "armor": 21.88,
    #     "magic_resist": 30,
    #     "movement_speed": 340
    # }
]

def remove_champion(champions:list):
    print("\n-- SUPPRIMER UN CHAMPION --\n")

    response = input("Retirer quel champion (id) : ")

    try:
        index = int(response)
        champions.pop(index - 1)
        return champions
    except:
        print("\n[ERREUR] entrer l'index d'un champion pour le supprimer")
        return champions

def add_champion(champions):
    print("\n-- NOUVEAU CHAMPION --\n")

    response = input("Entrer les informations en respectant cet ordre (nom, classe, pv, regeneration_pv, mana, regeneration_mana, portee, attaque, vitesse_attaque, armure, resistance_magique, vitesse_deplacement)\n-> ")
    args = response.split(" ")

    if len(args) != 12:
        print("\n[ERREUR] le nombre de paramètre requis est incorrect")
        return champions
    
    champ = {
        "name": args[0],
        "class": args[1],
        "hp": args[2],
        "hp_regen": args[3],
        "mana": args[4],
        "mana_regen": args[5],
        "range": args[6],
        "attack_damage": args[7],
        "attack_speed": args[8],
        "armor": args[9],
        "magic_resist": args[10],
        "movement_speed": args[11]
    }

    print("\nChampion cree avec succes")
    return champions.append(champ)

def champion_battle(champions):
    print("\n-- DUEL DE CHAMPIONS --\n")

    first_id = input("Choix du premier champion (id) : ")
    
    try:
        champions[int(first_id)]
    except:
        print("\n[ERREUR] entrer l'index d'un champion de la liste")
        return
    
    second_id = input("Choix du second champion (id) : ")

    try:
        champions[int(second_id)]
    except:
        print("\n[ERREUR] entrer l'index d'un champion de la liste")
        return

    first_champ = champions[int(first_id)]
    second_champ = champions[int(second_id)]
    selection = [first_champ, second_champ]
    current_champion_index = selection.index(random.choice(selection))

    while first_champ["hp"] > 0 and second_champ["hp"] > 0:
        if current_champion_index == 0:
            second_champ["hp"] -= first_champ["attack_damage"]
            current_champion_index += 1
        else:
            first_champ["hp"] -= second_champ["attack_damage"]
            current_champion_index-= 1
        
        print(f"{first_champ['name']} {'0' if first_champ['hp'] < 0 else round(first_champ['hp'])} - {second_champ['name']} {'0' if second_champ['hp'] < 0 else round(second_champ['hp'])}")
    
    if first_champ['hp'] > 0:
        print(f"\nGAGNANT : {first_champ['name']}")
    else:
        print(f"\nGAGNANT : {second_champ['name']}")

def show_champions(champions):
    print("\n-- LISTE DES CHAMPIONS --")

    response = input("\nTaper l'index du champion pour voir toutes ses informations\nAppuyer sur 'Entree' pour voir la liste complète des champions : ")

    try:
        index = int(response)
        champion = champions[index - 1]
        
        print(f"\n\
  index                  : {index}\n\
  nom                    : {champion['name']}\n\
  classe                 : {champion['class']}\n\
  pv                     : {champion['hp']}\n\
  regeneration pv        : {champion['hp_regen']}\n\
  mana                   : {champion['mana']}\n\
  regeneration mana      : {champion['mana_regen']}\n\
  portee                 : {champion['range']}\n\
  degats d'attaque       : {champion['attack_damage']}\n\
  vitesse d'attaque      : {champion['attack_speed']}\n\
  armure                 : {champion['armor']}\n\
  resistance magique     : {champion['magic_resist']}\n\
  vitesse de deplacement : {champion['movement_speed']}")
        return
    except:
        pass

    if (response == ""):
        for index,champion in enumerate(champions):
            print(f"{index + 1} : {champion['name']}")

if __name__ == '__main__':
    response = requests.get("https://raw.githubusercontent.com/ngryman/lol-champions/master/champions.json")
    
    lol_champions = json.loads(response.content)

    for champion in lol_champions:
        champions.append({
            "name": champion["name"],
            "class": champion["tags"][0],
            "hp": champion["stats"]["hp"],
            "hp_regen": champion["stats"]["hpregen"],
            "mana": champion["stats"]["mp"],
            "mana_regen": champion["stats"]["mpregen"],
            "range": champion["stats"]["attackrange"],
            "attack_damage": champion["stats"]["attackdamage"],
            "attack_speed": champion["stats"]["attackspeed"],
            "armor": champion["stats"]["armor"],
            "magic_resist": champion["stats"]["spellblock"],
            "movement_speed": champion["stats"]["movespeed"]
        })
    
    while True:
        print("\nMenu")
        response = input("\
  1. Liste des champions\n\
  2. Ajouter un champion\n\
  3. Retirer un champion\n\
  4. Combat de 2 champions\n\
  5. Quitter\n\n\
Choix : ")

        try:
            int(response)
        except:
            print("\n[ERREUR] il faut entrer un entier")
            continue
        
        choice = int(response)

        if (choice == 1):
            show_champions(champions)
        elif (choice == 2):
            champions = add_champion()
        elif (choice == 3):
            champions = remove_champion(champions)
        elif (choice == 4):
            champion_battle(champions)
        elif (choice == 5):
            break
        else:
            print("[\nERREUR] choisir une des options proposées (1, 2, 3)")
            continue