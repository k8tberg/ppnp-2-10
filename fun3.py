a = 10
b = 10


def dodaj():
    a = 6
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)  # wykona sie na wartościach globalnych


def dodaj3():
    global a  # brane do funkcji 'a' globalne
    a = 6
    b = 7
    print(a + b)


print("Zmienna a z góry", a) #Zmienna a z góry 10
dodaj() #13
print("Zmienna a z góry", a)
dodaj2() # 20
print("Zmienna a z góry", a)
dodaj3() #13
print("Zmienna a z góry", a) #Zmienna a z góry 6