import Csoport

# eljárások
adatokListaja=[]
def beolvasas():
    beFajl = open("csoport.txt", "r", encoding="utf-8")
    # első sor
    beFajl.readline()
    # többi sor
    sorok = beFajl.readlines()
    for sor in sorok:
        # adatok tisztítás
        tisztitottSor = sor.strip()
        # print(tisztitottSor)
        daraboltSor = tisztitottSor.split("/")
        # print(daraboltsor)
        #példányosítás
        csoportTag = Csoport.Csoport(daraboltSor[0], daraboltSor[1], daraboltSor[2])
        # objektum listábafűzése
        adatokListaja.append(csoportTag)
        # print(csoportTag)
    beFajl.close()

def kiir():
    for index in range(0, len(adatokListaja), 1):
        print(adatokListaja[index])

def sorokSzama():
    sorszam = len(adatokListaja)
    print(f"A tanulók száma:{sorszam}")

def megszamlalas():
    osszeg = 0
    for index in range(0, len(adatokListaja), 1):
        osszeg += adatokListaja[index].atlag
    if len(adatokListaja) == 0:
        atlag = 0
    else:
        atlag = osszeg/len(adatokListaja)
    print(f"A suli átlaga: {atlag}")

def elsos():
    osszeg = 0
    for index in range(0, len(adatokListaja), 1):
            if adatokListaja[index].evfolyam == 1:
                osszeg += 1
    print(f"Első évfolyamosok száma: {osszeg}")


# főprogram
beolvasas()
kiir()
sorokSzama()
megszamlalas()
elsos()