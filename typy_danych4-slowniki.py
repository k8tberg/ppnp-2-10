# słownik - {klucz:wartosc}
# typ danych para: klucz - wartość
# odwzorowanie jsona w python
# {"name":"Radek"}
# klucz nie może się powtarzać

dictionary = {}  # pusty słownik
print(dictionary)  # {}
dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39  # {'imie': 'Radek', 'wiek': 39}
print(dictionary)

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 39)]) - lista z krotkami
dictionary.update({'date': '12-12.1203'})
print(dictionary)

dictionary1 = {'x': 2}
dictionary1.update([('y', 3), ('z', 5)])
print(dictionary1)
print(dictionary1['x'])  # 2 - wypisanie elementu ze słownika

# stworzenie słownika polsko - ang
# 3 klucze
# stworzyc slownik z elementami
# wypisać

dict2 = {'imie': 'name', 'kot': 'cat'}
print(dict2['imie'])
print("Mam w slowniku", dict2.keys())
key = input("Podaj słowko do przetłumaczenia: ")
# print(dict2[key])
print(dict2[key.replace(" ", "").lower()])

# kalkulator
# pobrać od usera a i b (input)
# wypisac wynik (print)

m = int(input("Podaj pierwszy wartosc: "))
#n = float(input("podaj druga wartość: "))
n = float(input("podaj druga wartość: "))
#dzial = input("jakie dzialanie: ")
# input zawsze zwraca string
print(type(m))
print(m + n)
print(m + int(n)) # alternatywna zamaiana typu danych










