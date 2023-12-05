def osztalybeir():
    kiFajl = open("fajl/proba.txt", "a", encoding="utf-8")
    kiFajl.write("\nSZF 13/B")
    kiFajl.close()
def kiir():
    beFajl = open("fajl/proba.txt", "r", encoding="utf-8")
    adatok = beFajl.read()
    print(adatok)
    beFajl.close()

    beFajl = open("fajl/proba.txt", "r", encoding="utf-8")
    beFajl.readline()
    print(beFajl.readline())
    beFajl.close()

    beFajl = open("fajl/proba.txt", "r", encoding="utf-8")
    elso5 = beFajl.read(5)
    print(elso5)
    beFajl.close()
