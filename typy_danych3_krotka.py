# krotka (tupla) - niezmienna lista
# jednoelementowa zmienna - niezmienna

temp = 37, 5
print(type(temp))
print((temp))

tupla2 = "Tomek", "Radek", "Zenek", "Marek"
tupla2a = ("Tomek", "Radek", "Zenek", "Marek")

print(tupla2.index("Tomek"))
print(tupla2.count("Tomek"))

print(type(tupla2a))
print(tupla2a)

tupla3 = 43, 55, 22.24, 11, 200
print(type(tupla3))

a, b = 1, 2
print(a)
print(b)
print(type((1,2))) # rozpakowanie tupli

# a, b = 1, 2, 3 #towyrzuca błąd, za dużo wartości niż zmiennych
a, *b = 1, 2, 3 # *  - worek na pozostałe elementy

print(a)
print(b)

print(tupla2)
*imie1, imie2, imie3 = tupla2
print(imie1)
print(imie2)
print(imie3)

lista = list(tupla3) #zamiana (rzutowanie) tupli na listę
print(lista) #[43, 55, 22.24, 11, 200]
print(type(lista)) <class 'list'>






