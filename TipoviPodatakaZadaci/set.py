#Opis: Imaš dve liste studenata koji su položili dva
# predmeta. Pronađi: Studente koji su položili oba predmeta
# (presek) Studente koji su položili bilo koji od predmeta (unija)
# Studente koji su položili samo matematiku Koristiš: set() za
# konverziju liste u skup, & za presek, | za uniju, - za razliku.
# Napomena: Set automatski uklanja duplikate i ne garantuje
# redosled. Zato se ispis može razlikovati po redosledu.

matematika = ["Ana", "Marko", "Jelena", "Nikola", "Ivan"]
programiranje = ["Marko", "Jelena", "Petar", "Ivan", "Milan"]

m = set(matematika)
p = set(programiranje)

oba = m & p
print("Položili oba predmeta:", oba)

biloKoji = m | p
print("Položili bar jedan predmet:", biloKoji)

samoMatematika = m - p
print("Samo matematika:", samoMatematika)
