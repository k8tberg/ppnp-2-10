# ** argumenty slownikowe
def connect(**opcje):
    print(opcje)
    print(type(opcje))
    connect_param = {
        'host': "127.0.0.7",
        'port': '9090'
    }

    connect_param['pwd'] = opcje
    print(connect_param)
    print(connect_param['pwd']['klucz'])


# connect() # {} słownik
# {klucz: wartosc}
# klucz = wartosc

connect(klucz='wartosc')
connect(a1='2',klucz='wartosc')
connect(a1 ="2", klucz='wartość', a=98)

