class Car:
    """
    Klasa samochod
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # __ - pole prywatne --> hermetyzacja zmiennych w klasie

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Predkosc wynosi: {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car1 = Car("Fiat", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car1.__predkosc) # 50 - odczytujemy pole predkosc
# nie możemy odczytac bo zostalo oznaczone jako prywatne
car1.licznik()  # Predkość wynois: 50kh/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  #
car1.__predkosc = 100  # tak NIE robimy, mimo, ze Python technicznie to dopuszcza
car1.licznik()  # Prędkość wynosi: 100km/h, Prędkość wynosi 0km/h - po zmianie na pole prywatne
