# Dictionar

# Main program

keys = ("titlu","autor","limba","nr.pagini")
key_title = keys[0]
key_author = keys[1]
key_lang = keys[2]
key_pages = keys[3]
FRENCH = 'FR'

def ReadListOfBooks():
    list_carti = []

    while True:
        carte = input("Date carte: ").split(",")
        if carte == ['']:
            break
        dict_carte = dict()
        for i in range(4):
            dict_carte[keys[i]] = carte[i].strip()
        list_carti.append(dict_carte)
    return list_carti

list_carti = ReadListOfBooks()
print(list_carti)

# NrBooksDonation

def NrBooksDonation():
    list_donate = []

    for i in range(list_carti):

#


# print("Numarul de carti care se doneaza este: ",NrBooksDonation(list_carti))
# print("Autorii cartilor primite de catre Ion sunt: ", FrBooks(list_carti))
# print("Ion ramane cu urmatoarele carti: ", IonBooks(list_carti))