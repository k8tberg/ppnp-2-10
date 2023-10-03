dictionary = {'imie': 'Radek','nazwisko':"Kowalski"}
print(type(dictionary))

##wypisuje klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

for i in dictionary.values():
    print(i)

for k, v in dictionary.items():
    print(k, '=>', v)

dictionary2 = {'name':'imie', 'company':'rozne'}
print({value: key for key, value in dictionary2.items()}) #pivot
#{'imie': 'name', 'rozne': 'company'}
d2 = {}
for key, value in dictionary2.items():
    d2[value] = key #{'imie': 'name', 'rozne': 'company'}
print(d2)
print({value:key for key,value in dictionary2.items()})