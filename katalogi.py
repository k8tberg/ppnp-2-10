import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

print(base_path)
print(base_path2)

if base_path.exists() and base_path.is_dir(): #sprawdzamy czy jest taki plik  ikatalog, to go usuwamy, bo jesli by był, to rzuci bład
    shutil.rmtree(base_path) #usunięcie

base_path.mkdir()

path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

#path_b.mkdir()
# jesli by tak było to błąd: FileNotFoundError: [WinError 3] System nie może odnaleźć określonej ścieżki: 'ops_example\\A\\D'

path_b.mkdir(parents=True)
path_c.mkdir() #tu juz nie musimy parants, bo katalog A juz istnieje

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, 'w', encoding='utf-8') as stream:
        stream.write(f"Jakas tresc pliku {filename}")


shutil.move(path_b, path_d)
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / 'exrenamed.log')

print(base_path.absolute())
print(base_path2.absolute())
