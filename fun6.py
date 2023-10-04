# napisz funkcje obliczająca średnią
def liczby(i=0, *cyfry):  # *cyfry oznacza, ze mozemy wstawić nieokreslona ilosc argumentów
    print(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c  # suma = suma + c
        count = len(cyfry)
        avg = suma / count
    except Exception as e:
        print("Błąd", e)
    else:
        print(f"Srednia dla ucznia {i} wynosi {avg}")


liczby()  # łapie sie na wyjątek, bo dzielenie przez zero
liczby(1, 2, 3)
liczby("Adam", 2, 3, 4, 5, 6, 7, 8, 9)

