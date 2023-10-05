class Human:
    """
    Klasa opisująca człowieka w Pythonie
    """

    # konstruktor (inicjaliator)
    def __init__(self, imie, wiek, wzrost, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):  # self - rób na obiekcie, który Cię wywołał
        print(self)  # tylko wypisanie obiektu, niepotrzebnie tytaj
        print(f"Nazywam się {self.imie}")

    def podajw(self):  # self - rób na obiekcie, który Cię wywołał
        print(f"Mam {self.wiek} lat")

    def mojwzrost(self):  # self - rób na obiekcie, który Cię wywołał
        # print(f"Mam {self.wzrost} cm")
        print(f"Mój wzrost wynosi", self.wzrost, "cm")

    def wypiszplec(self):  # self - rób na obiekcie, który Cię wywołał
        # print(f"Mam {self.wzrost} cm")
        print(f"Płeć {self.plec}")

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Agata", 29, "178")
print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)
print(cz1.wzrost)
cz1.powitanie()
cz1.podajw()
cz1.mojwzrost()

cz2 = Human("Tomasz", 48, 190, "m")
cz2.powitanie()
cz2.podajw()
cz2.mojwzrost()

cz1.ruszaj()
cz2.ruszaj()
cz2.wypiszplec()

