import matplotlib.pyplot as plt

labels = ['2016','2017','2018','2019','2020','2021','2022','2023']
values = [10,20,30,25,35,40,30,25]

plt.bar(labels, values)
plt.title("Wykres słupkowy")
plt.xlabel('lata')
plt.ylabel('wartosci')

plt.show()
