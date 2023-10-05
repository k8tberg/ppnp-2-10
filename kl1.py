# klasa - szablon, wg którego budujemy obiekty, wskazujący jakie cechy będzie miał obiekt
# cechy - pola(zmienne)
# działania - funkcje
# obiekt - budowany na podstawie klasy (instancja klasy)

# definicja klasy
# PEP8 - wskauje, ze nazwy klasy z dużej litery
class Human:
    """
    Klasa opisująca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):  # self - rób na obiekcie, który Cię wywołał
        print(self) # tylko wypisanie obiektu, niepotrzebnie tytaj
        print(f"Nazywam się {self.imie}")
    def podajw(self):  # self - rób na obiekcie, który Cię wywołał
        print(f"Mam {self.wiek} lat")


print(Human.__doc__)  # wypisanie dokumentacji
# Klasa
# opisująca
# człowieka
# w Pythonie

print(print.__doc__)
# help(print)

cz1 = Human()
print(cz1)
print(cz1.plec)
cz1.imie = "Kasia"
cz1.wiek = 29
print(cz1.imie)
print(cz1.wiek)

# inny obiekt innej płci

cz2 = Human()
cz2.imie = "Tomek"
cz2.wiek = 87
cz2.plec = 'm'

print(cz2.imie)
print(cz2.plec)
cz1.powitanie()
cz1.podajw()

