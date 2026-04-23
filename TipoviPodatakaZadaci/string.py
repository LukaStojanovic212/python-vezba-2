#Opis: Program traži ime i prezime, pa ispisuje:
#Koristiš: .capitalize() ili .title(), len(),
# indeksiranje stringa ime[0], .replace(" ", "").

ime = input("Unesite ime i prezime: ")

imeFormatirano = ime.capitalize()
imeFormatirano2 = ime.title()
duzina = len(ime)
prvoSlovo = ime[0]
bezRazmaka = ime.replace(" ", "")

print("Formatirano:", imeFormatirano)
print("Formatirano sva velika:", imeFormatirano2)
print("Dužina:", duzina)
print("Prvo slovo:", prvoSlovo)
print("Bez razmaka:", bezRazmaka)
