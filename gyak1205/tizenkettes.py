def tk():
    adatokListaja = []
    beFajl = open("fajl/allas.txt", "r", encoding="utf-8")
    for sor in beFajl:
        # darabolás, tisztítás
        daraboltSor = sor.strip().split("  ")
        # print(daraboltSor)
        adatokListaja.extend(daraboltSor)
    beFajl.close()

    # feladat lényegi megoldása
    db = 0
    index = 0
    while index < len(adatokListaja):
        if adatokListaja[index] == "0":
            db += 1
        index += 1
    print(f"A ledöntött bábuk száma: {db}.")