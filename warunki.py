# instrukcje warunkowe - instrukcja sterowania przepływem programu
# if
# sterowana warunkiem, jeżeli warunek jest True to wykonuje działania z wydzielonego bloku
# odp = False
# if odp:
#     print(
#         "Brawo")  # wcięcie - standardowo 4 spacje, wszedzie gdzie ":" jest wymagana conajmniej jedna komenda we wcięciu
# else:
#     print("Musisz sie dalej uczy")
# print("Dzialam dalej")
#
# podatek = 0.0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
#
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(podatek)
# print(f"Podatek wynosi: {zarobki * podatek}")

suma_zam = 100
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabat wynosi {rabacik}")  # f - string format

rabat = 25 if suma_zam > 150 else 0
print(f"Rabat wynosi {rabat}")  # f - string format

lista_bledow = []  # pusta lista
# alert_system = "console"
alert_system = "email"
# alert_system = "inny"
# error = 'medium'
# error = "critical"
error = "inny"
error_message = "Stało się coś strasznego"

if alert_system == "console":
    print(error_message)
elif alert_system == 'email':
    lista_bledow.append("email")
    if error == 'medium':
        lista_bledow.append("ostrzezenie")
    elif error == "critical":
        lista_bledow.append("krytyczny")
    else:
        lista_bledow.append("inny blad")
else:
    print("Nieznany alert system")
print(lista_bledow)

a = 14
b = 3

print(f"Wynik porownania{a}>{b},{a > b}")
print(f"Wynik porownania{a}<{b},{a < b}")
print(f"Wynik porownania{a}>={b},{a >= b}")
print(f"Wynik porownania{a}<={b},{a <= b}")
print(f"Wynik porownania{a}=={b},{a == b}")
print(f"Wynik porownania{a}!={b},{a != b}")

# Wynik porownania14>3,True
# Wynik porownania14<3,False
# Wynik porownania14>=3,True
# Wynik porownania14<=3,False
# Wynik porownania14==3,False
# Wynik porownania14!=3,True
# napisac test z historii, geografii...whatever

#wyswietlic pytanie
# pobrac odpowiedz (print)
# sprawdzic odpowiedz (inpit)
# sparwdzic i wypisac

# pyt1 = "Data wojny ABC"
# odp1 = "1410"
#
# print(f"{pyt1}")
# odpu = (input(print(f"{pyt1}"))) ???
#
# if odp1 == odpu
#
odp = input ("Podaj cos")
if odp == '966':
    printf("Prawidlowo")
else:
    printf("zle")
