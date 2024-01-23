# # # calcul suma nr pare si impare dintr-o listasi diferenta lor

# # # citre n=
# # n = input("n=")
# # n = int(n)

# # lista_elemente = []

# # for el in range(n):
# #     el = input(f"{el} el = ")
# #     lista_elemente.append(int(el))

# # print(lista_elemente)

# # def sum_p(lista_elemente, i, n, sum):
# #     if i < n:
# #         if lista_elemente[i]%2 == 0:
# #             print(f"Suma {sum}")
# #             s = sum_p(lista_elemente, i+1, n, sum)
# #             sum += s
# #         else:
# #             s = sum_p(lista_elemente, i+1, n, sum)
# #             sum += s
# #     return sum

# # print(sum_p{[1,2,3,4], 0, 4, 0})

# # ####

# # def metoda_test(i,j):
# #     if i < 100 or j < 100:
# #         if i > j:
# #             print(i)
# #             metoda_test(i+1, j+2)
# #         elif j > i:
# #             print(j)
# #             metoda_test(i+2, j+1)
# #     print(i, j)

# # metoda_test(2,3)

# """
# Ex. 1
# Scrieti o functie recursiva ce returneaza diferenta 
# dintre suma el pare si cele impare dintr-un vector si afisati un mesaj dragut.
# * Afisati suma el pare 
# * Afisati suma ele impare
# * Afisati diferenta
# Ex:
#     [1,2,3,4]
#     sume el pare 2+4 = 6
#     sume le impare 1+3 = 4
#     diferenta=> 6-4 = 2
# """


# # Metoda 1
# def suma_p_i(lista, i, n, sum_p, sum_i):
#     print(f"Apelare suma_p_i nr. {i+1}")
#     if i < n:
#         if lista[i] % 2 == 0:
#             print(f"lista[{i}] = {lista[i]} este par.")
#             print(f"sum_p = {sum_p} + {lista[i]} = {sum_p+lista[i]}")
#             print("Se apeleaza suma_p_i\n")
#             sum_p_i = suma_p_i(lista, i + 1, n, sum_p + lista[i], sum_i)
#             print(
#                 f"Am revenit din metoda nr. {i+2} => metoda nr. {i+1} \n si returnez sum_p_i = {sum_p_i}\n"
#             )
#             return sum_p_i
#         else:
#             print(f"lista[{i}] = {lista[i]} este impar.")
#             print(f"sum_i = {sum_i} + {lista[i]} = {sum_i+lista[i]}")
#             print("Se apeleaza suma_p_i\n")
#             sum_p_i = suma_p_i(lista, i + 1, n, sum_p, sum_i + lista[i])
#             print(
#                 f"Am revenit din metoda nr. {i+2} => metoda nr. {i+1} \n si returnez sum_p_i = {sum_p_i}\n"
#             )
#             return sum_p_i
#     else:
#         print(f"Nu s-a indeplinit conditia i<n atunci: return {sum_p, sum_i}\n")
#         return sum_p, sum_i

lista = [1, 2, 3, 4]
# sum_p, sum_i = suma_p_i(lista, 0, len(lista), 0, 0)
# print(f"Suma el pare: {sum_p}")
# print(f"Suma el impare: {sum_i}")
###

# Metoda 2
# Avem doua metode recursive una pentru el pare si cealalta pentru el impare
def suma_p(lista, i, n, suma):
    print(f"Apelare suma_p nr. {i+1}")
    if i < n:
        if lista[i] % 2 == 0:
            print(f"lista[{i}] = {lista[i]} este par.")
            print(f"suma = {suma} + {lista[i]} = {suma+lista[i]}")
            print("Se apeleaza suma_p\n")
            suma = suma_p(lista, i + 1, n, suma + lista[i])
            print(
                f"Am revenit din metoda nr. {i+2} => metoda nr. {i+1} \n si returnez suma = {suma}\n"
            )
            return suma
        else:
            print(f"lista[{i}] = {lista[i]} este impar.")
            print("Se apeleaza suma_p\n")
            suma = suma_p(lista, i + 1, n, suma)
            return suma
    return suma

def suma_i(lista, i, n, suma):
    print(f"Apelare suma_i nr. {i+1}")
    if i < n:
        if lista[i] % 2 == 0:
            print(f"lista[{i}] = {lista[i]} este par.")
            print("Se apeleaza suma_i\n")
            suma = suma_i(lista, i + 1, n, suma)
            return suma
        else:
            print(f"lista[{i}] = {lista[i]} este impar.")
            print(f"suma = {suma} + {lista[i]} = {suma+lista[i]}")
            print("Se apeleaza suma_i\n")
            suma = suma_i(lista, i + 1, n, suma + lista[i])
            print(
                f"Am revenit din metoda nr. {i+2} => metoda nr. {i+1} \n si returnez suma = {suma}\n"
            )
            return suma
    return suma


sum_p = suma_p(lista, 0, len(lista), 0)
print(f"Suma el pare: {sum_p}")

sum_i = suma_i(lista, 0, len(lista), 0)
print(f"Suma el impare: {sum_i}")