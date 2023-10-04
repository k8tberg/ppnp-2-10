from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-10-04
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2023-10-04 09:55:14.941127
print(type(time))  # <class 'datetime.datetime'>

print(time.hour)
print(today.day)
print(today.year)

formatted_date = datetime.now().strftime('%d/%m/%Y')  # 04/10/2023
print(formatted_date)  # 04/10/2023

formatted_date = datetime.now().strftime("%H:%M")  # 10:08
print(formatted_date)

formatted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 2023-10-04 10:08:38
print(formatted_datetime)

# tomorrow = today + 1 #TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days = 0, seconds = 0, microseconds = 0

tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2023-10-05

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': today, 'price': 80.0},
    {'sku': 3, 'exp_date': tomorrow, 'price': 20.0},
    {'sku': 4, 'exp_date': today, 'price': 50},
]

print(products)

for product in products:
    print(product)
    if product['exp_date'] != today:
        continue  # nie wykonuj koljenych instrkukcji z pewtli, idz na poczatek petli, wez kolejny element

    product['price'] *= 0.8
    print(f"""
    Price for sku= {product['sku']}
    is now {product['price']}""")

# {'sku': 1, 'exp_date': datetime.date(2023, 10, 4), 'price': 100.0}
#
#     Price for sku= 1
#     is now 80.0
# {'sku': 2, 'exp_date': datetime.date(2023, 10, 4), 'price': 80.0}
#
#     Price for sku= 2
#     is now 64.0
# {'sku': 3, 'exp_date': datetime.date(2023, 10, 5), 'price': 20.0}
# {'sku': 4, 'exp_date': datetime.date(2023, 10, 4), 'price': 50}
#
#     Price for sku= 4
#     is now 40.0
