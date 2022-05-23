import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import math
import seaborn as sns

xlsx = pd.read_csv('flag.csv',header=0,sep=",",decimal='.')
df = pd.DataFrame(xlsx)
aaa = pd.DataFrame(xlsx)
print(df)
df2 = df[-75:]
print(df2)
a = df2.groupby(['religion']).agg({'population':['sum']})
a.plot(kind='bar',rot=45,figsize=(8, 8))
plt.ylabel('Ilość')
plt.xlabel("wiara")
plt.title('Wykres')
plt.legend(labels=[])
plt.show()
plt.savefig('Wykresik.png')


b = df[['religion','landmass']].groupby(['religion']).agg({'landmass':['sum']})
print(b)
b.plot(kind='pie',subplots=True,autopct='%.2f %%',figsize=(8, 8),fontsize=14)
plt.title('Tytuł')
plt.legend(loc=0)
plt.show()
df2 = df3 = df[-75:]
df2 = df2['area']
df3 = df3['population']
sns.set()
print(df2)
data = {'a': df2,
        'b': np.random.randint(25, 200, 75),
        'c': df3,
        'd': np.random.randint(75)}

df = pd.DataFrame(data)
plot = sns.relplot(data=df, x="a", y="b", hue="c",
palette='muted', size="d")
plot.fig.set_size_inches(10, 10)

plt.show()
