import requests as re
import xml.etree.ElementTree as ET

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'

response = re.get(url)
print(response)
xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)

table_name = root.find(".//Table").text
print(table_name)

date = root.find(".//EffectiveDate").text
print(date) #2023-10-06
no = root.find(".//No").text
print(f"Numer tabeli: {no}") #Numer tabeli: 194/A/NBP/2023
rates = root.findall(".//Rate")
print(type(rates)) #<class 'list'>

for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find("Code").text
    mid = rate.find("Mid")
    print(f"{code}: {currency} - {mid}")