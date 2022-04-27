import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000))
# print(ts)
ts = ts.cumsum()

# ts.plot()
# plt.savefig('wykres.png')
# plt.show()

# dane = {'Kraj':['Belgia','Indie','Brazylia','Polska'],
#         'Stolica':['Bruksela','New Delhi','Brasylia','Warszawa'],
#         'Populacja':[3,33,1,0],
#         'Kontynent':['Europa','Azja','Ameryka Południowa','Europa']}
# df = pd.DataFrame(dane)
# grupa = df.groupby('Kontynent').agg({'Populacja':['sum']})
# grupa.plot(kind='bar',ylabel='Kontynent',rot=0,title="Beeeeka",legend=True)
# plt.grid()
# plt.legend(loc='upper left')
# plt.show()

# df = pd.read_csv("dane.csv",header=0,sep=';',decimal=".")
# print(df)
#
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia':["sum"]})
# print(grupa)
#
# grupa.plot(kind='pie',subplots=True, autopct='%.2f %%',fontsize=20,figsize=(6,6))
# plt.legend(loc='upper left')
# plt.show()
#
df = pd.DataFrame(ts)
print(df)
df['Średnia krocząca'] = df.rolling(window=50).mean()
print(df)
df.plot()
plt.legend(['Średnia',"Średnia krocząca"])
plt.show()

