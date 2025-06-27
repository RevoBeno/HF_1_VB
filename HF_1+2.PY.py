from os.path import split


#1. Magánhangzó-számláló

def maganhango_szamlalo():

    mn_list = ["a","á","e","é","i", "í","o", "ó", "ö", "ő","u", "ú", "ü","ű"]

    #Neten néztem meg, hogy milyen megoldás van arra, hogy ne kelljen egyenként --> "Á" leírnom a karaktereket
    mn_string = "AÁEÉIÍOÓÖŐUÚÜŰ"
    mn_list2 = list(mn_string)

    db = 0
    szoveg = input("Adjon meg egy szöveget: ")
    for i in szoveg:
        if i in mn_list or i in mn_list2:
            db += 1
    print(f"{db} magánhangzó található.")

maganhango_szamlalo()

#2. Számjegyek összege

def szamjegyek_osszege():

    szam = int(input("Adjon meg egy számot: "))
    osszeg = 0

    strszam = str(szam)

    for i in strszam:
        osszeg += int(i)

    print(osszeg)
    print(type(osszeg))

szamjegyek_osszege()

#3 Szavak visszafelé

def szavak_visszafele():

    mondat = input("Adjon meg egy mondatot: ")
    szavak = mondat.split()
    for i in szavak[::-1]:
        print(i, end=" ")

szavak_visszafele()

#4 Leggyakoribb szám

def leggyakoribb_szam():

    szamok = []
    szam = int(input("Adjon meg egy számot: "))

    while szam != 0:
        szamok.append(szam)
        szam = int(input("Adjon meg egy számot vagy íron 0-át a kilépéshez: "))

        print(szamok)

    legnagyobb = 0
    for i in szamok:
        if i > legnagyobb:
            legnagyobb = i

    db = 0
    for j in szamok:
        if j == legnagyobb:
            db += 1

    print(f'A legnagyobb szám: {legnagyobb} és {db} db van belőle')
leggyakoribb_szam()

# 5. Egyszerű jelszó-ellenőrzés

def jelszo_ellenorzes():


    kisb = 'aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz'
    nagyb = 'AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ'
    szam = '123456789'

    while True:
        jelszo = input("Adjon meg egy jelszót: ")
        if len(jelszo) < 8:
            print("A jelszó karakterszáma kevesebb mint 8!")

            continue
        if not any(c in kisb for c in jelszo):
            print("A jelszónak tartalmaznia kell legalább 1 kisbetű")
            continue
        if not any(c in nagyb for c in jelszo):
            print("A jelszónak tartalmaznia kell legalább 1 nagybetű")
            continue
        if not any(c in szam for c in jelszo):
            print("A jelszónak tartalmaznia kell legalább 1 számot")
            continue

        print("A jelszó megfelelő!")
        break
jelszo_ellenorzes()