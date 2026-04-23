def saberi (a,b):
    return a + b

def oduzmi (a,b):
    return a - b

def pomnozi (a,b):
    return a * b

def podeli (a,b):
    return a / b

while True:
    print("1 - sabiranje")
    print("2 - oduzimanje")
    print("3 - mnozenje")
    print("4 - deljenje")
    print("0 - izlaz iz menija")

    odabir = int(input("Izberi neku od opcija: "))

    if odabir == 0:
        print("Kraj programa.")
        break
    if odabir in [1, 2, 3, 4]:

        a = int(input("Unesite vrednost a: "))

        b = int(input("Unesite vrednost b: "))

        if odabir == 1:
            print("Rezultat je: ", saberi(a,b))
        elif odabir == 2:
            print("Rezultat je: ", oduzmi(a,b))
        elif odabir == 3:
            print("Rezultat je: ", pomnozi(a,b))
        elif odabir == 4:
            print("Rezultat je: ", podeli(a.b))
        print("Sta zelite sledece da uradite?")
    else:
        print("Uneti broj je neodgovarajuc")
        break
