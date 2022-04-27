
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,header=0)
print(df)
a = df.groupby(['Rok']).agg({'Liczba':['sum']})
a.plot()
plt.show()

a = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(a)
a.plot(kind='bar')
plt.show()

a = df[df['Rok'] >2011].groupby(['Plec']).agg({'Liczba':['sum']})
a.plot(kind='pie',subplots=True,autopct='%.2f %%')
plt.show()

df = pd.read_csv('zamowienia.csv',header=0,sep=';',decimal=".")
print(df)
a = df.groupby(['Sprzedawca']).size()
a.plot(kind='bar',rot=30,figsize=(8,8),title="XDDDDDDDDDDDDD")
plt.tight_layout(h_pad=None)
plt.show()
