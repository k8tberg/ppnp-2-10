import csv

filename = 'record.csv'

fileds = []
rows = []

with open(filename, 'r', encoding="UTF-8") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024)) #1024 - przeszukuj w pierwszych 1024 znaków
    print(dialect.delimiter)
    print(dialect) #<class 'csv.Sniffer.sniff.<locals>.dialect'>
    csv_f.seek(0) #powrót na początej danych, ustawia licznik na 0
    #csvreader = csv.reader(csv_f, delimiter=";" )
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)

    fields = next(csvreader)  # odczyt pierwszego wiersza i ustawienie licznika na nastepny
    for row in csvreader:  # pętla startuje od indeksu 1, czyli drugiego wiersza
        rows.append(row)

print(fields)
print(rows)
suma = 0
for i in rows:
    number = float(i[-1])
    suma += number

print(f"Srednia wynosi {suma / len(rows)}") # Srednia wynosi 9.063333333333333
#
# 9.19
# 9.0
# 9