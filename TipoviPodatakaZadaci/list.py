#Opis: Napravi listu od 5 omiljenih filmova. Ispiši:
# Koliko filmova ima u listi Prvi i poslednji film
# Sortiranu listu po abecednom redu Listu obrnutim redom

filmovi = ["Iron men", "Captain America", "Thor", "Avengers", "Avengers:End game"]

print("Broj filmova:", len(filmovi))

print("Prvi film:", filmovi[0])
print("Poslednji film:", filmovi[-1])

sortirana = sorted(filmovi)
print("Sortirana lista:", sortirana)

obrnuta = list(reversed(filmovi))
print("Obrnuta lista:", obrnuta)
