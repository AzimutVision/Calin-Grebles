"""
Ex. 2
Avem o lista cu el. de tip int [232,3,55,22, -10,24]
a. Sa se creeze o metoda ce ordoneaza lista crescator
b. Sa se creeze o metoda ce ordoneaza lista descrescator
"""

# lista = [232,3,55,22, -10,24]

# def ord_cres(lista, i, n)
#     print(f"apelare ord_cres nr. {i+1}")
#     if i < n:
#         if lista[i] 

# lista_ord_cres = ord_cres(lista, 0, len(lista))

# for i in range(100):
#     print(i)
#     input('...')

# a.

lista = [232,3,55,22, -10,24]
print(lista)
for i in range(0, len(lista)):
    print(f"i este {i}")
    for j in range(i + 1, len(lista)):
        print(f"j este {j}")
        if lista[i] > lista[j]:
            x = lista[i]
            print(f"x este {x}")
            lista[i] = lista[j]
            lista[j] = x
print(lista)

# for i in range(len(lista)):
#     print(i)
#     print(lista[i])

# b.
for z in range(0, len(lista)):
    for y in range(z + 1, len(lista)):
        if lista[z] < lista[y]:
            p = lista[z]
            lista[y] = lista[z]
            lista[y] = p

print(lista)



