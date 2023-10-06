import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0,1,1000)
print(type(data))

plt.hist(data, bins=30)
plt.title("Histogram")
plt.ylabel('Czestość')
plt.xlabel('Wartość')

plt.savefig("wykres.png")
plt.savefig("wykres.pdf")
plt.show()