# while - pętla sterowana warunkiem
# instrukcja sterowania przepływem programu
# dopoki True petla sie wykonuje

licznik = 0
while True:
    licznik += 1 #licznik = licznik +1
    print("Komunikat")
    if licznik >10:
        break #przerywa działanie te pętli

print("Dalsza część programu")
licznik = 0
while licznik < 11:
    print("Komunikat!!!")
    licznik +=1

lista = []
lista2 = []

while True:
    wej = input("Podaj liczbe")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista) #['2', '4', '3']
print(lista2) #[2, 4, 3]
