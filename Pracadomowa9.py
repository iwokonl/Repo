# numpy 1.22.2
# pandas 1.4.0
# openpyxl 3.0.9

import numpy as np
import pandas as pd
print("Zad 1")
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,header=0)
print(df)
print(df.where(df['Liczba']>1000))
print(df.where(df['Imie']=='Iwo'))
print(df.groupby(['Rok']).agg({'Liczba':['sum']}))
print(df.groupby(['Plec']).agg({'Liczba':['sum']}))
print(df.groupby(['Rok','Plec']).agg({'Liczba':['sum']}))
print(df.sort_values(by='Liczba',ascending=False).groupby(['Plec']).head(1))

print("Zad 2")
df = pd.read_csv('zamowienia.csv',header=0,sep=";",decimal='.')
print(pd.unique(df['Sprzedawca']))
print(df.sort_values(by='Utarg',ascending=False).head(5))
print(df['Sprzedawca'].value_counts(ascending=False))
print(df.where((df['Data zamowienia'] > '2005-01-01') & (df['Data zamowienia'] < '2005-12-31') & (df['Kraj']=='Polska')).count())
print(df.where((df['Data zamowienia'] > '2004-01-01') &(df['Data zamowienia'] < '2004-12-31') & (df['Utarg'])).mean())
a = df.where((df['Data zamowienia'] > '2004-01-01') &(df['Data zamowienia'] < '2004-12-31') & (df['Utarg'])).mean()
b = df.where((df['Data zamowienia'] > '2005-01-01') & (df['Data zamowienia'] < '2005-12-31') & (df['Kraj']=='Polska')).count()
a.to_csv('plik1.csv', index=False)
b.to_csv('plik2.csv', index=False)
