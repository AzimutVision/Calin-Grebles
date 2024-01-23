"""
Ex. 3
Avem o lista cu el de tip string
a. Sa se creeze o metoda ce ordoneaza lista alfabetic
b. Sa se creeze o metoda ce ordoneaza lista invers alfabetic
"""

lista = ["sad", "a", "f", "ntrbbadvfvs"]

# a.

for i in range(0, len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            x = lista[i]
            lista[i] = lista[j]
            lista[j] = x

print(lista)

for i in range(0, len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] < lista[j]:
            x = lista[i]
            lista[i] = lista[j]
            lista[j] = x

print(lista)