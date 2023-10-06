class Dom:
    """
    Klasa opisujaca Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):  # __init__ konstruktor
        # uzupełnić konstruktor
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

        # stworzyć metody odczytujące te pola

    def podaj_kolor(self):
        print(f"Kolor {self.__kolor}")

    def podaj_metraz(self):
        print(f"Metraz {self.__metraz}")

    def podaj_okna(self):
       print(f"Mam {self.__liczba_okien} okien")


    def zmien_kolor(self):
        wybor = input("Podaj kolor")
        self.__kolor = wybor
        self.podaj_kolor()
        self.__farba()
    def zmien_metraz(self):
        wybor = float(input("Podaj metraz"))
        self.__metraz = wybor
        self.podaj_metraz()

    def zmien_okna(self):
        wybor = int(input("Podaj okna"))
        self.__liczba_okien = wybor
        self.podaj_okna()

    def __farba(self):
        print("Skończyła się farba")


dom1 = Dom(150, "biały", 10)
dom1.podaj_okna()
dom1.podaj_metraz()
dom1.podaj_kolor()

dom1.zmien_kolor()
# Mam 10 okien
# Metraz 150
# Kolor biały
# Podaj kolorbiały
# Kolor biały
# Skończyła się farba

