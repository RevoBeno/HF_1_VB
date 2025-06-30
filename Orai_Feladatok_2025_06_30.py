
def szorzat():

    nr_1 = float(input("Adj meg egy számot: "))
    nr_2 = float(input("Adj meg még egy számot: "))
    szorzas = nr_1 * nr_2
    print(f'A két szám szorzata {szorzas}')

szorzat()

def kisebb_dupla():

    nr1 = int(input("Adj meg egy számot: "))
    nr2 = int(input("Adj meg még egy számot: "))

    kisebb = 0

    if nr1 < nr2:
        kisebb = nr1 * 2
        print(f'A két szám közül a kisebb duplája: {kisebb}')
    else:
        kisebb = nr2 * 2
        print(f'A két szám közül a kisebb duplája: {kisebb}')

kisebb_dupla()

def paros_paratlan():

    while True:
        szam = input("Adjon meg egy egész számot: ")
        if szam == "":
            break
        if int(szam) % 2 == 0:
            print("A megadott szám páros")
        else:
            print("A megadott szám páratlan")

paros_paratlan()
print("................................")
def nagyobb_tripla():

    nr_1 = float(input("Adj meg egy számot: "))
    nr_2 = float(input("Adj meg még egy számot: "))
    nagyobb = 0
    if nr_1 < nr_2:
        nagyobb = nr_2 * 3
        print(f'A két szám közül a nagyobb háromszorosa: {nagyobb}')
    else:
        nagyobb = nr_1 * 3
        print(f'A két szám közül a nagyobb háromszorosa: {nagyobb}')

nagyobb_tripla()
