#Program traži cenu proizvoda
#i procenat popusta, pa ispisuje konačnu cenu.

cena = int(input("Unesite cenu proizvoda: "))
popust = int(input("Unesite procenat popusta: "))

iznosPopusta = cena * popust // 100
novaCena = cena - iznosPopusta

print("Cena sa popustom je:", novaCena)
