def nyolc():
    # beolvasás
    beFajl = open("fajl/dal.txt", "r", encoding="utf-8")
    fajlTartalma = beFajl.read()

    beFajl.close()

    dbk = 0
    dbK = 0
    fajltartalmaUj = ""
    for index in range(0, len(fajlTartalma), 1):
        if fajlTartalma[index] == "k":
            dbk += 1
            fajltartalmaUj += "*"
        elif fajlTartalma[index] == "K":
            dbK += 1
            fajltartalmaUj += "*"
        else:
            fajltartalmaUj += fajlTartalma[index]
    print(f"Cenzúrázott fálj tartalma:{fajltartalmaUj}")
    print(f"k betűk száma: {dbk}, K betű"
          f"k száma: {dbK}")
