def beir():
    kiFajl = open("fajl/proba.txt", "a", encoding="utf-8")
    kiFajl.write("\nSZF 13/B")
    kiFajl.close()

def kiir():

    beFajl = open("fajl/dal.txt", "r", encoding="utf-8")
    beFajl.readline()
    masodikSor = beFajl.readline()
    beFajl.close()

    beFajl = open("fajl/dal.txt", "a", encoding="utf-8")
    beFajl.write(masodikSor)

def kiir2():
    beFajl = open("fajl/dal.txt", "r", encoding="utf-8")
    adatok = beFajl.read()
    print(adatok)
    beFajl.close()

