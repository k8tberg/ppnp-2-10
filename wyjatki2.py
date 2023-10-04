# kalkulator na match case
#

while True:
    print(f"""
    1. dodawanie
    2. odejmowanie
    3. mnożenie
    4. dzielenie
    5. koniec""")

    odp = input("Podaj operacje:")
    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("podaj drugą liczbę"))

        match odp:
            case '1':
                print(f"Wynik dodawania {a} + {b} ={a + b}")
            case '2':
                print(f"Wynik odejmowania {a} - {b} ={a - b}")
            case '3':
                print(f"Wynik dodawania {a} * {b} ={a * b}")
            case '4':
                print(f"Wynik dodawania {a} / {b} ={a / b}")
            case _:
                print("Coś poszło nie tak")
                break


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
