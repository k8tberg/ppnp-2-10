# klasa abstrakcyjna - klasa, z której nie można stworzyc obiektu
from abc import ABC, \
    abstractmethod  # pakiet abc i klasa ABC, która pozwala tworzyć klasy abstrakcyjne. Nasze klasy po niej dziedziczą


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pytonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lecę z szybkościa", self.szybkosc)

    @abstractmethod  # oznaczylismy metodę jako abstrakcyjną
    def wydaj_odglos(self):
        pass


class Kura(Ptak):  # dziedziczenie po Ptaku
    """
    Kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print(f"Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("kokokokoko")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print(f"piiiii")


# po dodaniu @abstractmethod klasa Ptak staje sie abstrakcyjną, bo posada metodę abstrakcyjną


# orz1 = Ptak("orzeł", 20)
# orz1.latam()  # Tu orzeł lecę z szybkościa 20
# kur1 = Ptak("Kura", 0)
# kur1.latam()
# kur1.wydaj_odglos()
# kur2 = Ptak("Kura", 0)
# kur3 = Kura("Kura")
# print(kur2.gatunek)
# kur2.latam()

kur2 = Kura("Kura")
print(kur2.gatunek)
kur2.latam()
orz3 = Orzel("Orzel", 20)
orz3.latam()
print(orz3.gatunek)
orz3.wydaj_odglos()
