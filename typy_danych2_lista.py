# lista - kolekcja przechowująca dowolną ilość danych
# przechwouje różne typy danych w jednej kolejkcji
# lista zachowuje koljeność dodawania elementów

lista = [] #definicja pustej listy
print(list)
print(type(lista))

print(bool(lista))
lista.append("Radek")
print(lista)

lista.append("Maciej")
lista.append("Jaś")
lista.append("Staś")
lista.append("Ola")

print(lista)

#ostatni element listy ma rowniez index -1
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
# print(lista[10]) # bład, bo nie ma takiego rekordu
print(len(lista))
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])

print(lista[0:3]) # z lewej jest zawsze zbiór zamknięty, a z prawej otwarty
print(lista[2:]) # od 2 do końca
print(lista[:3]) # od 0 do 2
print(lista[7:9]) # pusto, ale bez błedu
print(lista[1:3])

lista[2] = "Mikołaj"
print(lista)

# rozszerzenie listy w konkretne miejsce
lista.insert(1, "Marcin") # 1 - to numer indeksu, który uzyska ten wstawiony rekord
print(lista)

ind = lista.index("Marcin")
print(ind)

#usunięcie elementu po indeksie
element = lista.pop(ind)
print(lista)
print(element)

#usunięcie po elemencie
element = lista.remove("Maciej")
print(lista)
print(element)
print(bool(None))

print('Radek' in lista)
lista.append('Radek') #  usuwa pierwszy napotkany
print(lista)

a = 1
b = 3
a = b
a = 7

lista2 = lista # kopiuje referencję (adres pamieci)
print(lista)
print(lista2)

lista.clear() # czyści zwartość listy
print(lista)
print(lista2)
lista3 = lista.copy() # kopiuje jedną listę do drugiej
print(id(lista2))
print(id(lista))
print(id(lista3))
liczby = [54, 999, 34, 22, 13.34, 687]
# liczby = [54, 999, 34, 22, 13.34, 687, "A"] # da bład przy sortowaniu
print(liczby)
print(type(liczby))
liczby.sort()
print(liczby)

lista_osob = ['rade', 'ola', 'ala', 'ania']
lista_osob.sort()
lista_osob.sort(reverse=True)
print(lista_osob)
lista_osob.reverse()
print(lista_osob)
liczby[3] = 6666
print(liczby) # [13.34, 22, 34, 6666, 687, 999]

print(liczby[0:3])
print(liczby[0:-2]) # 0...4
print(liczby[-3:0]) # w zasadzie błędny zapis bo nie moze z -3 dojsc do zera poruszając się w prawą stronę
print(liczby[-3:])
liczby.remove(34)
print(liczby)
print(liczby.pop(3)) #687

tekst = "Python"
lista_1 = list(tekst) #rozpakowanie sekwencji
print(lista_1) # ['P', 'y', 't', 'h', 'o', 'n']

lista2 = [tekst]
print(lista2) # ['Python']
print(lista_1 + lista2) # ['P', 'y', 't', 'h', 'o', 'n', 'Python']

krotka = tuple(liczby)
print(krotka)




