# pliki csv
# pliki tekstowe, gdzie dane oddzielone są separatorem
# Radek, Maciek, Zenek

import csv

row = ['radek', 'coe', 3, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']
dict2 = dict(zip(fields, row))
print(dict2)  # {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.1'}

dict_x = [
    {'name':'radek', 'branch':'coe','year':3, 'cgpa':'9.19'},
    {'name':'tomek', 'branch':'coś','year':2, 'cgpa':'9.0'},
    {'name':'kasia', 'branch':'cor','year':2, 'cgpa':'9'},

]
filename = 'record.csv'
with open(filename, 'w', encoding='utf-8', newline='') as csv_f:
    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(row) #zapisanie wiersza z listy

    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=';')
    csvwriter.writeheader()  # zapisanie nazw kolumn
    #csvwriter.writerow(dict2)  # zapisanie wiersza ze słownika
    csvwriter.writerows(dict_x)  # zapisanie wiersza ze słownika

