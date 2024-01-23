"""
Ex. 4
a. Avem o lista cu mai multe elemente [1,2,3, 'a', 'abc', -12, [1,2, 'a']]
* Se citeste x de la tastatura si se cauta in lista definita mai sus.
* In cazul in care ele se gaseste in lista sa se afiseze pozitia acestuia ex:
    Input: x =  'a'
    Output: Elementul 'a' se afla pe pozitia 3

b. problema a. dar recursiv
"""
# a.

lista = [1,2,3, 'a', 'abc', -12, [1,2, 'a']]

# x = input(f"Introduceti un string de la tastatura: ")

# for i in range(0, len(lista)):
#     if x == lista[i]:
#         print(i)

# b.
x = input(f"Introduceti un string de la tastatura: ")

def metoda(lista, i, n, x):
    if i < n:
        if x == lista[i]:
            print(f"Elemntul a este pe pozitia: ", i)
        else:
            metoda(lista, i + 1, n, x)


metoda(lista, 0, len(lista), x)

