# napisac aplikacje kalkulator
# wykorzystac jako głowna pętle programu while
# pobrac rodzaj operacji, 5 wyjscie z programu
# pobrac liczny
# wyswietlic wynik

while True:
    print(f"""
    1. dodawanie
    2. odejmowanie
    3. mnożenie
    4. dzielenie
    5. koniec""")

    odp = input("Podaj operacje:")
    if odp >= '5':
        print("nie mam takiego działania")
        break
    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("podaj drugą liczbę"))

        if odp == '1:':
            print("Wynik", a + b)
        elif odp == '2':
            print("Wynik", a - b)
        elif odp == '3':
            print("Wynik", a * b)
        elif odp == '4':
            print("Wynik", a / b)
        else:
            print("cos poszło nie tak")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Błąd wartości")
    except Exception as e: #łapie pozostałe wyjątki
        print ("Błąd", e)
    else:
        print("Gdy nie ma błędu") # wykonuje sie tylko gdy nie ma błędu
    finally:
        print("Zawsze")
