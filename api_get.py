# REST API - GET, POST, PUT, DELETE, [HEAD]
# odpowiednik w bazie danych: select, insert, update, delete
# CRUD - create, read, updte, delete
import requests as re
# pip install request
#url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'
#url = 'http://api.nbp.pl/api/exchangerates/rates/A/THB/'
url = 'http://api.nbp.pl/api/exchangerates/tables/B/'
response =re.get(url)
print(response)
# <response [200]> -- ok
# 3XX - błedy konfiguracji np przekierowania
# 4XX - 404 - bład zasobu, 400 Bad request
# 5XX - wewnetrzne błedy serwera, np. błąd bazy danych

table = response.json()
print(table)

#<Response [200]> {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD', 'rates': [{'no': '193/A/NBP/2023', 'effectiveDate': '2023-10-05', 'mid': 4.3768}]}

print(table['table'])
print(table['currency'])
print(table['code'])
print(table['rates']) #[{'no': '193/A/NBP/2023', 'effectiveDate': '2023-10-05', 'mid': 4.3768}]
print(table['rates'][0])
print(table['rates'][0]['no'])
print(table['rates'][0]['effectiveDate'])
print(table['rates'][0]['mid'])

