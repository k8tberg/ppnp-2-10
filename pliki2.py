# odczytać plik w Pythonie
import chardet
# pip install chardet - w terminalu mozemy wykorzystć taka komende

file_path = 'test.log'
with open(file_path, 'rb') as file: #rb - odczytaj binarnie
    raw_data = file.read()

print(raw_data)
result = chardet.detect(raw_data)
print(result)
#{'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''} - to jest słownik
kodowanie = result['encoding']
confidence = result['confidence']
print(kodowanie, confidence) # utf-8 0.87625
print(raw_data.decode(encoding=kodowanie))

# {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}
# utf-8 0.87625
# Radek
# dodane
# dośdane
# dośdane
# dośdane