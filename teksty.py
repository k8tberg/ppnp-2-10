tekst = "Witaj swiecie"
print(tekst)
print(type(tekst))  # <class 'str'>

tekst2 = tekst.upper()  # zamiana tekstu na duze litery
print(tekst2)
print(tekst)
# teksty sa immutable (niezmienne) niemutowalne
print(tekst.lower())
print(tekst.removeprefix("Witaj"))
print(tekst.removesuffix("swiecie"))
print(tekst.removesuffix("swiecie").upper())

encoded_s = tekst.encode('utf-8')
print(encoded_s)
print(type(encoded_s))
print(encoded_s.decode('utf-8'))

print(tekst[0])
print(tekst.count("i"))
print(tekst.count("i",0,4))
print(tekst.count("j",0,4))

print(len(tekst))

imie = "Kasia"
tekst_format = f"Mam na imię {imie} i lubie Pythona"

print(tekst_format)
tekst_format = f"\tMam na imię {imie}\n i lubie Pythona \b"
print(tekst_format)

starszy = "Witaj %s"
print(starszy % imie)

print(""" 
    Tekst
wielolinijkowy""")

print("Witaj {}".format(imie))