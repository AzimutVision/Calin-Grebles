# 1. Variabile și Atribuire
# Declarați o variabilă nume și atribuiți-i numele dvs.
nume = "Calin"
# Declarați o variabilă varsta și atribuiți-i vârsta dvs.
varsta = 37

# 2. Tipuri de Date și Conversii
# Calculați anul nașterii folosind variabila varsta.
anul_curent = 2024
anul_nasterii = anul_curent - varsta
# Afișați anul nașterii.
print(anul_nasterii)

# 3.Operatori Aritmetici
# Declarați o variabilă pret și atribuiți-i o valoare.
pret = 10
# Declarați o variabilă cantitate și atribuiți-i o valoare.
cantitate = 3
# Calculați costul total folosind operatori aritmetici.
cost_total = pret * cantitate
print(f"pretul total este: {cost_total}")

# 4.Operatori de Comparare
# Comparați valoarea costului total cu o sumă fixă și afișați un mesaj în funcție de rezultat.

suma_fixa = 20
rezultat_1 = (cost_total < suma_fixa)
print(f"{cost_total} este mai mic decat {suma_fixa}? {rezultat_1}")
rezultat_2 = (cost_total > suma_fixa)
print(f"{cost_total} este mai mare decat {suma_fixa}? {rezultat_2}")
rezultat_3 = (cost_total == suma_fixa)
print(f"{cost_total} este egal cu {suma_fixa}? {rezultat_3}")

