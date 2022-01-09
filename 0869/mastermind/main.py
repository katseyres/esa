import random

LIFES = 20
COLORS = {
    "A": "azure",
    "B": "brown",
    "C": "cyan",
    "D": "desert",
    "E": "emerald",
    "G": "green",
    "M": "magenta",
    "O": "orange",
    "P": "purple",
    "R": "red",
    "W": "white",
    "Y": "yellow",
}
ROW_LENGTH = 5
HIDDEN_PLACE = "."
GOOD_PLACE = "V"
GOOD_COLOR = "O"

def randomRow():
    randomC = []
    for i in range(ROW_LENGTH):
        randomC.append(random.choice(list(COLORS.keys())))
    return randomC

def askRow(hiddenRow, rRow):
    print("\n--- COLOR CODE ---")
    for key in COLORS:
        print(f"| ({key}) {COLORS[key]}")
    print("------------------")
    
    return list(input(f"\nCreate a color line of {ROW_LENGTH} elements: ").upper())

def checkColor(randomRow:list, pawn:str):
    return randomRow.__contains__(pawn)

def checkPosition(randomRow:list, pawn:str, position:int):
    return randomRow[position] == pawn

def checkRow(randomRow:list, row:list, hiddenRow:list):
    print("");

    if len(row) != ROW_LENGTH:
        print(f"/!\ Row must have exactly {ROW_LENGTH} pawns.")
        return list(HIDDEN_PLACE * len(randomRow))

    for index,pawn in enumerate(row):
        if COLORS.keys().__contains__(pawn) is False:
            print(f"/!\ [{pawn}] No color assigned for this letter.")
            return list(HIDDEN_PLACE * len(randomRow))
                
        if checkColor(randomRow, pawn) is False:
            # print(f"|--> [{pawn}] Random row has not this color.")
            hiddenRow[index] = HIDDEN_PLACE
        else:
            # print(f"|--> [{pawn}] Random row has this color.")
            hiddenRow[index] = GOOD_COLOR

            if checkPosition(randomRow, pawn, index):
                # print(f"|--> [{pawn}] Good position for the pawn {index + 1}")
                hiddenRow[index] = GOOD_PLACE
        
    return hiddenRow


rColors = randomRow()
hiddenRow = list(HIDDEN_PLACE * len(rColors))
myRow = askRow(hiddenRow, rColors)

hiddenRow = checkRow(rColors, myRow, hiddenRow)
rowsHistoric = {}
lifesUsed = 0

while (hiddenRow.__contains__(HIDDEN_PLACE) or hiddenRow.__contains__(GOOD_COLOR)) and lifesUsed < LIFES:
    rowsHistoric[lifesUsed] = {
        "input": " ".join(myRow),
        "output": " ".join(hiddenRow)
    }
    
    print("\n--- HISTORIC ---")
    for key in rowsHistoric:
        print("{} [{}] {}".format(LIFES - key, rowsHistoric[key]["input"], rowsHistoric[key]["output"]))
    print("----------------")

    lifesUsed += 1
    myRow = askRow(hiddenRow, rColors)
    hiddenRow = checkRow(rColors, myRow, hiddenRow)

if lifesUsed == LIFES:
    print("Il ne vous reste plus de vies, solution: {}".format(" ".join(rColors)))
else:
    print("\nRow found: {}".format(" ".join(rColors)))