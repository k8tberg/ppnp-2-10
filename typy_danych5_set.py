# set, zbiór - przechowuje niepowtarzające sie elementy
# tracimy kolejność przy dodawaniu


lista = [44, 55, 66, 77, 33, 22, 11, 33, 11]
zbior = set(lista)  # zamiana listy na zbior
print(zbior)  #
print(type(zbior))
zb2 = set()  # pusty zbiór
print(zb2)  # set()

zbior.add(33)  #dodawanie elementu do zbioru
zbior.add(18)
zbior.add(18)

print(zbior) #{33, 66, 11, 44, 77, 18, 22, 55}, dane w zbiorze nie mają indeksów
zbior.remove(55)

print(zbior)
print(zbior.pop()) # usuniecie pierwszego elementu, 33
print(zbior)
print(len(zbior))
print(type(zbior))

lista2 = list(zbior)
print(lista2)

zbior2 = {66,11,44,18, 52, 62, 999, 999} # mozna tez tak stworzyc tak zbior. Python odrozni od slownika, bo nie ma par klucz:wartosc
print(zbior2)
print(type(zbior)) #<class 'set'>
print(zbior | zbior2) # suma zbiorow {66, 999, 11, 44, 77, 18, 52, 22, 62}
print(zbior & zbior2) #czesc wspolna {18, 66, 11, 44}
print(zbior - zbior2) #roznica {77, 22}
print(zbior.difference(zbior2)) #roznica {77, 22}
print(zbior2.difference(zbior)) #roznica
print(zbior) #{66, 11, 44, 77, 18, 22}
print(zbior2) #{66, 18, 52, 999, 11, 44, 62}



