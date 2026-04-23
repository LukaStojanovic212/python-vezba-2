print("Unosi brojeve, zavrsno sa nulom: ")

suma = 0
count = 0

while True:
    broj = int(input())

    if broj == 0:
        break

    suma += broj
    count += 1

if count > 0:
    prosek = suma / count
    print("Prosek je: ", prosek)
else:
    print("Nema unetih brojeva")