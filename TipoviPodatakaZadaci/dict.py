#Opis: Napravi rečnik sa podacima o državama (država →
# glavni grad). Program treba da: Ispiše sve države i
# glavne gradove. Pita korisnika za državu i vrati glavni grad
# Ako država ne postoji, ispiši poruku. Koristiš: definisanje
# rečnika, prolazak for drzava, grad in drzave.items(), provera
# if drzava in drzave, pristup drzave[drzava].
drzave = {
    "Srbija": "Beograd",
    "Francuska": "Pariz",
    "Italija": "Rim",
    "Nemačka": "Berlin",
    "Španija": "Madrid"
}

print("Države i glavni gradovi:")
for drzava, grad in drzave.items():
    print(drzava, "→", grad)

unos = input("\nUnesite državu: ")

if unos in drzave:
    print("Glavni grad je:", drzave[unos])
else:
    print("Ta država ne postoji u bazi.")
