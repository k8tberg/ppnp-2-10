import os # biblioteka do pracy z plikami

for root, dirs, files in os.walk(".."): # przyszła krotka, którą rozpakowalismy
    abs_root = os.path.abspath(root)
    print(abs_root)

    #wyciągamy katalogi

    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_) #dir - slowo zakazane, więc dodajemy podłogę, jesli koniecznie chcemy tego użyć

    if files:
        print("Files:")
        for filename in files:
            print(filename)

for root, dirs, files in os.walk("..\ppnp-2-10"):
    for file in files:
        if file =='api_get.py':
            file_path = os.path.join(root, file)
            print(file_path) #../ppnp-2-10\api_get.py