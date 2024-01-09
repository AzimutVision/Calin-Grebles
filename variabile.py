variabila_1 = 1
variabila_2 = 'a'
print(variabila_1)
print(variabila_2)
#
# numere intregi (INTEGER):
varsta = 37
anul_nasterii = 1986
anul_curent = 2023
varst_input = anul_nasterii - anul_curent
print(anul_curent - anul_nasterii)

"""
siruri de caractere
"""
nume = "Calin \" "
prenume = "Grebles"
print(nume + prenume)
print(f"{nume} {prenume}")
print(f"Salut {nume} {prenume}!")

'''exercitiu de printat'''

v_1 = 1
v_2 = 2
v_3 = "A"
v_4 = v_1 + v_2
print(f"{v_3} = {v_4}")
print(v_3 , "=" , v_4)

# Numere reale (FLOAT)

# variabila de tip boolean (BOOL)

adevarat = True
fals = False
print(adevarat, " ", fals)

# liste

lista_piese_auto = ["carburator", "roti", "volan"]
print(lista_piese_auto)
print(lista_piese_auto[0])

lista_piese_auto.append("cutie_de_viteze")
print(lista_piese_auto)

lista_scaune_auto = ["scaun_sofer", "scaun_pasager", "scaun_copil"]
lista_piese_auto.insert(0,"motor")
print(lista_piese_auto)
lista_piese_auto.insert(4, lista_scaune_auto)
print(lista_piese_auto)
lista_piese_auto.extend(lista_scaune_auto)
print(lista_piese_auto)

# actualizarea elementelor in lista
lista_scaune_auto[1] = "bancheta_spate"
print(lista_piese_auto)

# stergerea datelor

del lista_piese_auto[0]
print(lista_piese_auto)

# printare indexi lista - subsiruri/feliere/sliceing

lista_numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_numere[0:11:2])
print(lista_numere[-3:-1])
print(lista_numere[0:-1])

lista_caractere = ["unu", "doi", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua", "zece"]
print(lista_caractere[0:11:2])

# lungimea listei

print(f"Lungimea listei {lista_numere} de numere este: {len(lista_numere)}")
print(f"Lungimea listei {lista_numere} de numere din 2 in 2 este: {len(lista_numere[0:11:2])}")

# tuples

tuple_numere = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple_caractere = ("unu", "doi", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua", "zece")
print(tuple_numere)
print(tuple_caractere)

# dictionaries

persoana_1 = {
    "nume": "Calin",
    "varsta": 37,
    "prenume": "Grebles"
}
print(persoana_1)
print(persoana_1["varsta"])

# accesarea elementelor
print(f"varsta: {persoana_1.get('varsta')}")

print(f"nume: {persoana_1['nume']}")

# stergerea elementelor
del persoana_1["varsta"]
print(persoana_1)

