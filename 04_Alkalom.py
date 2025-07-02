
#1. feladat
def megszamlalas():

    list = [0] * 11

    while True:
        szam = input("Adj meg egy számot: ")

        if szam == "":
            print("A program kilépett!")
            break

        szam = int(szam)
        if szam >= 1 and szam <= 10:
            list[szam] += 1
        else:
            print("Csak 1 és 10 közötti számokat adhat meg!")

    for i in range(1,11):
        print(f'{i}: {list[i]} db')

megszamlalas()

#2. Feladat

def szokoev():

    while True:
        ev = (input("Adj meg egy évszámot: "))

        if ev == "":
            print("A program kilépett!")
            break
        ev = int(ev)
        if (ev % 4 == 0 and ev % 100 != 0) or ev % 400 == 0:
            print("Szökőév")
        else:
            print("Nem szökőév")

szokoev()

#3. Feladat

def atlag_szamolas(szamok):

    szamok = [24, 31, 22, 43, 10, 84, 38, 44, 84, 56, 67, 51, 56, 84, 31, 65,
              69, 83, 39]

    def atlag(szamok):
        return sum(szamok) / len(szamok)

    def kisebb_szuresek(szamok, minel):
        szurt = []
        for i in szamok:
            if i < minel:
                szurt.append(i)
        return szurt

    def atlagnal_kisebbek(szamok):
        return kisebb_szuresek(szamok, atlag(szamok))

    pass

#4. Feladat

def csere(szo, hol, mire):

    if hol < 0 or hol >= len(szo):
        raise ValueError("Érvénytelen pozicíó: " + str(hol)) #TODO:tetszőleges error visszadobása
    return szo[0:hol] + mire + szo[hol + 1:]


def negyedik_feladat():
    uj = csere("répa", 1, "i")
    print(uj)

    try:
        #TODO: Kipróbálás
        uj = csere("teszt", -1, "X")
        print(uj)
    except ValueError as e:
        pass
negyedik_feladat()
