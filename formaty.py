import sys

user = "Tomek"  # str
wiek = 39  # int
wersja = 3.110001  # float - l.zmiennoprzecinkowe
liczba = 134567456234  # int
print(sys.int_info)
print("Witaj %s masz teraz %d lat" % (user, wiek))
# print("Witaj %s masz teraz %d lat" %(wiek, user)) #nie zgadzaja sie typy

print("Witaj %(user)s, masz teraz %(age)d lat." % {"user": user, "age": wiek})
print("Witaj {} masz teraz {} lat.".format(user, wiek))
print("Witaj {} masz teraz {} lat.".format(wiek, user))

print(f"Witaj {user}, masz teraz {wiek} lat.")

print("Uzywamy wersji Pythona %i" % 3)
print("Uzywamy wersji Pythona %f" % 3.11)
print("Uzywamy wersji Pythona %.1f" % 3.11)
print("Uzywamy wersji Pythona %.2f" % 3.11)
print("Uzywamy wersji Pythona %.0f" % 3.11)
print("Uzywamy wersji Pythona %.f" % 3.11)
print("Uzywamy wersji Pythona %.f" % 3.9)

x = 3.14
print("Zero miejsc po przecinku %.f" % x)
print("Oryginalny x =", x)

print(f"Uzywany wersji Pythona {wersja}")
print(f"Uzywany wersji Pythona {wersja:.1f}")
print(f"Uzywany wersji Pythona {wersja:.0f}")

print(f"{user:>10}")
print(f"{user:>20}")
print(f"{user:<30}")
print(f"{user:^30}")  # wyśrodkowanie

print(liczba)
print("Nasza duża liczba{:,}".format(liczba))
print("Nasza duża liczba{:,}".format(liczba).replace(",", "."))
print("Nasza duża liczba{:,}".format(liczba).replace(",", " "))

print(f"Nasza duża liczba{liczba:,}")
print(f"Nasza duża liczba{liczba:,}".replace(",", " "))
