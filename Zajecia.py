import numpy as np
import pandas as pd


#Tworzenie serii danych
# s = pd.Series([0,5,5.5,np.nan,'a'])
# print(s)
#
# s1 = pd.Series([16,15,8,14],index=['a','b','c','d'])
# print(s1)
#
# #Ramka danych(data frame)
#
# dane = {'Kraj':['Belgia','Indie','Brazylia'],
#            'Stolica':['Bruksela','New Delhi','Bresilia'],
#            'Populacja':[11190846,1421243213,287847528]}
# df = pd.DataFrame(dane)
# print(df)
# print(df.dtypes)
#
# daty = pd.date_range('20220420',periods=5) #tworzenie dat
# print(daty)
# df2 = pd.DataFrame(np.random.randn(5,4),index = daty,columns=list('ABCD')) # pd.DataFrame(matrix,index=,columns=)
# print(df2)
#
# #Otwarcie pliku .csv
#
# df = pd.read_csv('iris.csv',header=0,sep=',',decimal='.')
# print(df)
# df.to_csv('nowy.csv',index=False)
#
# #Otwarcie pliku .xlsx(wymagana biblioteka openpyxl)
# xlsx = pd.ExcelFile('wyniki.xlsx')
# df = pd.read_excel(xlsx,header=0)
# print(df)
#
# df.to_excel('nowy.xlsx',sheet_name='arkusz1',index=False)


#DOSTĘP DO DANYCH, odwolywanie sie do poszczegolnych elementow

# print(s1['a'])
# print(s1.a)
# print()
#
# print(df['Stolica'])
# print()
# print(df.iloc[[0]])
# print()
# print(df.loc[[0],['Kraj']])
# print()
# print(df.at[0,'Kraj']) #takie same dzialanie jak .loc()
# print()
# print('kraj: '+df.Kraj)
# print()
# print(df.sample(3))
#
# print(df.sample(frac=0.5)) # wartosc procentowa wszystkich wynikow
# print()
# print(df.sample(10,replace=True)) # z powtarzaniem sie elementow
# print()
# print(df.head()) # pobieranie początkowych n elementow
# print(df.head(2))

# irisdf = pd.read_csv('iris.csv',header=0,sep=',',decimal='.')
# print(irisdf)
# print(irisdf.head(10))
# print(irisdf.tail(10)) # drukuje n ostatnich wierszy


#FILTROWANIE DANYCH
# print()
# print(s1)
# print(s1[(s1 > 9)]) # nazwaSeriiDanych[(nazwaSeriiDanych + warunek)], wyswietla elementy ktore maja wartosc wieksza od 9
# print()
# print(s1.where(s1 > 14,'element za maly'))
# seria = s1.copy()
# print()
# print(seria)
# seria.where(seria > 10,'element za maly',inplace=True) # operacja ma zostac od razu wykonana bez kopii danych, nasza seria zostanie zmodyfikowana
# print(seria)
# print()
# print(s1[~(s1 > 14)])
# print()
# print(s1[~(s1 < 15) & (s1>8)])
# print()
# print(df[df['Populacja'] > 120000000])
# print()
# print(df[((df.Populacja > 1000000) & (df.index.isin([0,2])))])
#
# szukaj = ['Belgia','Brasilia']
# print(df.isin(szukaj)) # zwracane jako kopia

#DODAWANIE ELEMENTOW
#Seria danych
# print()
# s1['e'] = 15
# print(s1)
#
# #Ramka danych
# #w ramkach nalezy pamietac aby dodawac na poszczegolnych kolumnach dane typu dla danej kolumny
# df.loc[5] = 'nowy element' # takie dodawanie elementow nie jest wskazana dla ramki danych
# df.loc[4] = ['Polska','Warszawa',38675467]
# print(df)
# print()
#
# #Usuwanie elementow z dataFrame
# df.drop([5],inplace=True) #wiersz
# print(df)
# print()
# # df.drop('Kraj',axis=1,inplace=True) # usuniecie kolumny
# # print(df)
#
# df['Kontynent'] = ['Europa','Azja','Ameryka Południowa','Europa'] #dodanie kolumny
# print(df)
# print()
#
# #SORTOWANIE DANYCH
# print(df.sort_values(by='Kraj'))
#
# print()
# #GRUPOWANIE DANYCH
# grupa = df.groupby(['Kontynent'])
# print(grupa.get_group('Europa'))
# print()
# print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))

df = pd.ExcelFile('imiona.xlsx')
dane = pd.read_excel(df,header=0)
#print(dane)

#Zadanie 2
print(dane[dane['Liczba'] > 1000])
print(dane[dane['Imie'] == 'PAWEL'])
print(dane.agg({'Liczba':['sum']}))
print(dane[((dane['Rok']>=2000) & (dane['Rok']<=2005))].agg({'Liczba':['sum']}))
print(dane.groupby(['Plec']).agg({'Liczba':['sum']}))
print(dane.groupby(['Rok','Plec']).max())
