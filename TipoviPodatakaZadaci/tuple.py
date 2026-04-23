#Napravi tuple sa RGB bojom (npr. (255, 128, 0) -
# narandžasta). Program ispisuje pojedinačno R, G i B
# vrednosti i pokušava da izmeni jednu vrednost - pokaži
# šta se dešava. Koristiš: tuple sintaksu (a, b, c), unpacking
# r, g, b = boja, indeksiranje. Napomena: Razlika od liste -
# tuple je nepromenljiv (immutable). Ovo je namerno u zadatku -
# pokaži sebi da ne može da se menja (koristi try/except ili
# samo izazovi grešku i vidi šta se dogodi).

boja = (255, 128, 0)

r, g, b = boja

print("R:", r)
print("G:", g)
print("B:", b)

print("R preko indeksa:", boja[0])
print("G preko indeksa:", boja[1])
print("B preko indeksa:", boja[2])

try:
    boja[0] = 100
except TypeError as e:
    print("Greška:", e)
