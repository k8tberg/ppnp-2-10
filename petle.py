import random
from itertools import zip_longest

# petle
# instrukcja sterowania przepływem
# for - pętla iteracyjna

for i in range(10):  # 0...9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # _ niema zmienna
    pass

lista2 = list(range(1, 50))  # 1....49
for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)

for i in range(10):
    print(i * 2)

for i in range(10):
    if i % 2 == 0:  # warunek na liczbe parzysta
        print(i, "Parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

lista4 = []
for j in range(10):
    if j % 2 == 0:
        lista4.append(j)
print(lista4)  # [0, 2, 4, 6, 8]

for c in lista4:
    if c == 2:
        c += 1  # c = c + 1
    print(c)
a = 1
a += 1  # a = a + 1
print(a)
a -= 1  # a = a - 1
print(a)
a *= 3  # a = a*3
print(a)
a %= 2  # a = a%2 - reszta z dzielenia
print(a)
a /= 2  # a = a/2
print(a)  # 0.5 float - wynik dzielenia to zawsze jest float

imiona = ["Radek", "Asia", "Zbyszek", "Karolina"]
for p in imiona:
    print(p)

for p in range(len(imiona)):
    print(p, imiona[p])

for p in imiona:
    print(imiona.index(p), p)

# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Karolina

# enumarete() - zwraca ponumerowane elementy kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Asia')
# (2, 'Zbyszek')
# (3, 'Karolina')

a, b = (0, "Radek")
print(a)
print(b)

for p, w in enumerate(imiona):  # rozpakowanie krotki
    print(p, w, sep=";", end='')

print()

# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Karolina
# spacje pomiędzy liczba a imieniem domyślnie

ludzie = ['Radek', 'Zenek', 'Andrzej', 'Karolina', 'Kasia']
wiek = [47, 67, 43, 32]

# # wypisać osobe i jej wiek
# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])
#     # bład rozne wielkosci list

# zip() - łączy kolekcje
for k in zip(ludzie, wiek):
    print(k)  # ('Karolina', 32)
# 0,w = k gdzie k to krotka ('Karolina', 32)

for o, w in zip(ludzie, wiek):
    print(o, w)

# Radek 47
# Zenek 67
# Andrzej 43
# Karolina 32

for p in enumerate(zip(ludzie, wiek)):
    print(p)  # (3, ('Karolina', 32))

a, b = (3, ('Karolina', 32))  # rozpakowanie ponumerowanej i połączonej krotki
print(a, b)
c, d = b  # rozpakowanie krotki ludzie wiek
print(a, c, d)

# analogicznie zrobić w pętli tak by dla wszystkich elementów to sie wykonało (4)

for a, (c, d) in enumerate(zip(ludzie, wiek), start=1):  # start=1 zapewnia "wyliczanie" od 1, a nie zero
    print(a, c, d)

# 0 Radek 47
# 1 Zenek 67
# 2 Andrzej 43
# 3 Karolina 32

# petle
# instrukcja sterowania przepływem
# for - pętla iteracyjna

for i in range(10):  # 0...9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # _ niema zmienna
    pass

lista2 = list(range(1, 50))  # 1....49
for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)

for i in range(10):
    print(i * 2)

for i in range(10):
    if i % 2 == 0:  # warunek na liczbe parzysta
        print(i, "Parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

lista4 = []
for j in range(10):
    if j % 2 == 0:
        lista4.append(j)
print(lista4)  # [0, 2, 4, 6, 8]

for c in lista4:
    if c == 2:
        c += 1  # c = c + 1
    print(c)
a = 1
a += 1  # a = a + 1
print(a)
a -= 1  # a = a - 1
print(a)
a *= 3  # a = a*3
print(a)
a %= 2  # a = a%2 - reszta z dzielenia
print(a)
a /= 2  # a = a/2
print(a)  # 0.5 float - wynik dzielenia to zawsze jest float

imiona = ["Radek", "Asia", "Zbyszek", "Karolina"]
for p in imiona:
    print(p)

for p in range(len(imiona)):
    print(p, imiona[p])

for p in imiona:
    print(imiona.index(p), p)

# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Karolina

# enumarete() - zwraca ponumerowane elementy kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Asia')
# (2, 'Zbyszek')
# (3, 'Karolina')

a, b = (0, "Radek")
print(a)
print(b)

for p, w in enumerate(imiona):  # rozpakowanie krotki
    print(p, w, sep=";", end='')

print()

# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Karolina
# spacje pomiędzy liczba a imieniem domyślnie

ludzie = ['Radek', 'Zenek', 'Andrzej', 'Karolina', 'Kasia']
wiek = [47, 67, 43, 32]

# # wypisać osobe i jej wiek
# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])
#     # bład rozne wielkosci list

# zip() - łączy kolekcje
for k in zip(ludzie, wiek):
    print(k)  # ('Karolina', 32)
# 0,w = k gdzie k to krotka ('Karolina', 32)

for o, w in zip(ludzie, wiek):
    print(o, w)

# Radek 47
# Zenek 67
# Andrzej 43
# Karolina 32

for p in enumerate(zip(ludzie, wiek)):
    print(p)  # (3, ('Karolina', 32))

a, b = (3, ('Karolina', 32))  # rozpakowanie ponumerowanej i połączonej krotki
print(a, b)
c, d = b  # rozpakowanie krotki ludzie wiek
print(a, c, d)

# analogicznie zrobić w pętli tak by dla wszystkich elementów to sie wykonało (4)

for a, (c, d) in enumerate(zip(ludzie, wiek), start=1):  # start=1 zapewnia "wyliczanie" od 1, a nie zero
    print(a, c, d)

# 0 Radek 47
# 1 Zenek 67
# 2 Andrzej 43
# 3 Karolina 32

jezyk = ['python', 'java']
zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='Nan') # zip_longest to jest iterator, dlatego musimy zamienic na liste
print(type(zipped))
zipped_list = list(zipped) # zamieniamy na liste

for item in zipped_list:
    (print(item))

for o, w, j in zipped_list:
    print(o, w, j)
