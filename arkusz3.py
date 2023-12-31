import pandas as pd
import numpy as np
import openpyxl

technologies = ['Spark', 'Pandas', "Python", "PHP"]
fee = [25000, 20000, 15000, 18000]
duration = ['50 Days', '35 Days', np.nan, '30 Days', '30 Days']
columns = ['Courses','Fee','Duration','Discount']
discount = [2000, 1000, 800, 500, 500]

df = pd.DataFrame(
    list(zip(technologies, fee, duration, discount)),
    columns=columns
)

print(df)
df.to_excel('Courses.xlsx')
df.to_excel('Courses.xls', engine='openpyxl')
