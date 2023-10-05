import pandas as pd #alias pandas - biblioteka do data science
#pip install pandas - alternatywne dodanie biblioteki

data = pd.read_csv('record.csv', delimiter=";")
print(data)

#     name branch  year  cgpa
# 0  radek    coe     3  9.19
# 1  tomek    coś     2  9.00
# 2  kasia    cor     2  9.00

print(data.columns)
print(data.values)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
# [['radek' 'coe' 3 9.19]
#  ['tomek' 'coś' 2 9.0]
#  ['kasia' 'cor' 2 9.0]]
# to są listy, ale nie pythonowe

print(type(data.values)) # <class 'numpy.ndarray'>
print(data.values[0])
print(data.items)

# <bound method DataFrame.items of     name branch  year  cgpa
# 0  radek    coe     3  9.19
# 1  tomek    coś     2  9.00
# 2  kasia    cor     2  9.00>


