#Opis: Program traži cenu proizvoda i procenat popusta,
#pa ispisuje konačnu cenu. Koristiš: float() za konverziju,
#množenje, round() za zaokruživanje na 2 decimale.

cena = float(input("Unesite cenu proizvoda: "))
popust = float(input("Unesite procenat popusta: "))

iznosPopusta = cena * popust / 100
novaCena = cena - iznosPopusta

novaCena = round(novaCena, 2)

print("Cena sa popustom je:", novaCena)

#mozemo da stavimo {novaCena:.2f} da zaokruzimo na 2 decimale