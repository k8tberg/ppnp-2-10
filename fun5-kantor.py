# funkcje kantor
# usd, eur

# def kantor(waluta, kwota):
#     print("uruchomienie kantoru:")
#
#     def usd():
#         print(f"wymieniam dolary",{kwota * 4.4})
#
#
#     def eur():
#         print(f"Wymieniam euro",{kwota * 4.3})
#
#     if waluta == 'eur':
#         return eur
#     else:
#         return usd
#
# money = kantor("usd", 1000)
# print(money) #<function kantor.<locals>.usd at 0x0000017276996F20>
# money(1000) #wymieniam dolary

# przerobic tak, by funkcje wew przyjmowały kwoty do wumiany
# wypisac
# wymieniam dolary: 1000 usd = 4300 pln

def kantor(waluta):
    print("uruchomienie kantoru:")

    def usd(kwota):
        print(f"wymieniam dolary", {kwota}, "dolary to", {kwota * 4.4})

    def eur(kwota):
        print(f"Wymieniam euro: {kwota} eur = {kwota * 4.6} pln ")

    if waluta == 'eur':
        return eur
    else:
        return usd


money = kantor("eur")
print(money)  # <function kantor.<locals>.usd at 0x0000017276996F20>
money(10000)  # wymieniam dolary
