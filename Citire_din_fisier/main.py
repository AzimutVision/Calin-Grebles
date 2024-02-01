file = "C:\\Calin-Grebles\\Fisierul_de _citit\\fisier.txt" # pe windows trebuie \\ slashuri duble pt ca altfel se interpreteaza fiind string
#read from file
# f = open(file, "r")
# print(f.read(5))

# # readline
# f = open(file, "r")
# print(f.readlines())

# # linie cu linie
# f = open(file, "r")
# for x in f:
#     print(x)
# f.close() # inchidem fisierul dupa ce l-am deschis pentru ca ocupa memorie

# # append
# f = open(file, "a")
# f.write("\ntext din append")

# with open(file, 'r') as f: # with inchide automat fisierul dupa ce ruleaza
#     # print(f.read())
#     var_a = f.read()

# print(var_a)


# path
# import os
# # sys.path.append(path)
# print(os.getcwd())

import json

# with open('fisiere_json\\fisier.json') as f:
#     data = json.load(f)

# print(data['nume'])


# dictionar = {"name": "Ion", "animale": "pesti"}
# dictionar["key"] = "value"

# with open('fisiere_json\\fisier.json', 'w') as f:
#     json.dumps(dictionar, f)

# with open("balamuc.txt", 'w') as f:
#     f.write("Este un fisier creatde python?")


import random

l1 = ['1', '2', '3', '4']
l2 = ['8', '7', '5', '6']

V1 = l1[random.randrange(0,len(l1))]
print(V1)