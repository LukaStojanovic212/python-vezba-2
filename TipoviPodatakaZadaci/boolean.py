#Opis: Program proverava da li se korisnik može učlaniti
# u teretanu. Pravila: mora imati 16+ godina I imati saglasnost
# (ako je mlađi od 18). Koristiš: bool varijable, logičke
# operatore and, or, upoređivanje stringa sa "da".
# Napomena: Rezultat treba da bude True ili False -
# direktan ispis bool varijable.

godine = int(input("Unesite godine: "))
saglasnost = input("Da li imate saglasnost roditelja (da/ne): ")

imaSaglasnost = bool(saglasnost == "da")

moze = bool(godine >= 16 and (godine >= 18 or imaSaglasnost))

print(moze)
