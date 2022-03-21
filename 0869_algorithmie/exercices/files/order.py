from count_letters import FileService

DATA_PATH = "./data.csv"
BILL_PATH = "./bill.txt"
TVA = 0.21

def read_csv(path:str):
    output = []
    
    with open(path, "r") as file:
        table = file.read().split("\n")
        for line in table[1:]:
            fields = line.split(";")
            row = {}
            for i,field in enumerate(fields):
                try:
                    field = float(field)
                except:
                    if field.isdecimal():
                        field = int(field)

                row[table[0].split(";")[i]] = field
            output.append(row)

    return output

def get_values(data:list, key:str):
    output = []
    for d in data:
        output.append(d[key])
    return output

def total_price(prices:list, quantities:list, tva:float):
    return sum((prices[i] + prices[i] * tva) * quantities[i] for i in range(len(prices)))   

def sub_total(price:int, quantity:int, tva:float):
    return round((price * quantity + price * quantity * tva), 2)

if __name__ == "__main__":
    data = read_csv(DATA_PATH)
    prices = get_values(data, "price")
    quantities = get_values(data, "quantity")
    total = total_price(prices, quantities, TVA)
    sub_tot = (sub_total(prices[i], quantities[i]) for i in range(len(data) - 1))

    bill = ""
    for row in data:
        bill += f"Vous avez commande {round(row['quantity'])} unite{'s' if row['quantity'] > 1 else ''} de l'article \"{row['label']}\" au prix unitaire de {row['price']} euros, ce qui revient a un prix total, pour l'article, de {sub_total(row['price'], row['quantity'], TVA)} euros (TVAC).\n"
    
    bill += f"\nLe prix total de la facture s'eleve a {total} euros."

    FileService.write(BILL_PATH, bill)
