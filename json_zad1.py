# json -{"name":"Radek"}
# obiekt typu klucz wartość

import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

dict_json = json.dumps(person_dict)  # {"name": "Radek", "age": 40, "czy_pali": null} - zamiana danych na słownik w formacie json
print(dict_json)  #
print(type(dict_json))

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True) #zapisanie danych

with open('nasze_dane.json', 'r') as f:
    data = json.load(f)

print(data)
print(type(data))
