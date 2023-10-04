# funkcja - wydzielony kod programu, który mozna wykonywać wielokrotnie

a = 6
b = 7


# definicja funckji, tu funkcja sie nie wykonuje
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # funkcja z dwoma argumentami, obowiązkowe a i b przy wywołaniu
    print(a + b)


def odejmij(a, b, c=0):  # arg c ma wartość domyślną; w celu uzyskania efektu przeciążania argumentów funckji (symulowanie przeciazania arg funk)
    print(a - b - c)


def odejmij2(liczba1, liczba2):
    print(liczba1 - liczba2)


# wywołanie funckji (uruchomienie)
dodaj()  # 13
dodaj2(6, 5)
# dodaj2() #TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
odejmij(1, 2)
odejmij(1, 2, 7)  # przekazywanie pozycyjne
odejmij(b=6, a=8, c=1)  # argumenty nazwane
odejmij2(4, 5)
odejmij2(liczba2=10, liczba1=25)
#odejmij(c=11, 2, 8) #SyntaxError: positional argument follows keyword argument
#print(dodaj() + dodaj2(5,7)) #TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

print(dodaj()) # funkcja nic nie zwraca wyniku, tylko wypisuje