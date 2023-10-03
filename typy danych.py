wiek = 47
rok = 2023
temp = 36.6
wiek2 = 37.5

print(wiek)
print(type(wiek))
print(5 * "wiek")

print(wiek * rok)
print(wiek + rok)
print(wiek - rok)
print(wiek / rok)  # zawsze wunikiem dzielenia jest float
print(wiek // rok)  # czesc całkowita dzielenia
print(wiek % rok)
print(5 % 2)  # 1 - reszta z dzielenia
print(wiek ** rok)
print(54 - 5 * 43 + 4 / 2 + 4 / 2)
print(54 - (5 * 43) + (4 / 2 + 4) / 2)

print(0.2 + 0.8)
print(0.2 + 0.7)
print(0.2 + 0.7 + 0.8)
print(0.3 + 0.6 + 0.7)

# typ logiczne
# True i False - z dużej litery!!!
czy_znasz_pythona = True
print(czy_znasz_pythona)
print(int(czy_znasz_pythona))  # int() - zamiana (rzutowanie) na int

x = -10

print(bool(x))  # bool() - zamiana na typ logiczny; nie-zero zawsze jest True, zero jest False
x = 'radek'
print(bool(x))
x = ''
print(bool(x))
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)