# python 3.10
# match case

lista = []
lang = input("Podaj znany Ci jezyk programowania: ")

match lang.lower().replace(" ", ""):
    case "python":
        lista.append(lang)
    case "c++":
        lista.appned(lang)
    case "java":
        lista.append(lang)
    case _:  # wartośc domyślna (odpowiednik else)
        print("nie znam takiego działania")


print(lista)