def create_set(s):
    set_returned = set()
    for obj in s.split(','):
        set_returned.add(obj.strip())
    return set_returned

set_mama = create_set(input("Lista mamei: "))
set_ana = create_set(input("Lista Anei: "))
set_maria = create_set(input("Lista Mariei: "))

print(set_mama)
print(set_ana)
print(set_maria)

set_cumparaturi = set_ana | set_maria # union
print("S-au cumparat: ", set_cumparaturi)

# Ce mai e de cumparat?
set_rest_cumpraturi = set_mama - set_cumparaturi
if set_rest_cumpraturi == set():
    print("Nu mai sunt cumparaturi de facut.")
else:
    print("Mai avem de cumparat: ", set_rest_cumpraturi)
# Ce s-a cumparat in plus?
set_in_plus = set_cumparaturi - set_mama # set_cumparaturi.difference(set_mama)
if set_in_plus == set():
    print("Nu sunt cumparaturi in plus.")
else:
    print("S-a cumparat in plus: ", set_in_plus)


# Care elemente sunt duplicate?

set_duplicate = set_ana & set_maria
if set_duplicate == set():
    print("Nu avem duplicate.")
else:
    print("Avem duplicate: ", set_duplicate)

