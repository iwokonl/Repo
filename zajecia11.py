
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import math
import seaborn as sns

# plt.plot((np.arange(1,21,1)), (1/(np.arange(1,21,1))), "g:>")
# plt.legend(labels=['f(x)=x'])
#
# # plt.plot((np.arange(1,20,0.1)),(np.sin(np.arange(1,20,0.1))))
# # plt.plot((np.arange(1,20,0.1)),(np.cos(np.arange(1,20,0.1))))
# # plt.xticks(np.arange(1,20,2))
# # # plt.legend(labels=['cos', 'sin'],loc="upper right")
# # csv = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
# # df = pd.DataFrame(csv)
# #
# #
# # x = df['sepal length']
# # y = df['sepal width']
# # z = np.random.randint(0, 150,150)
# # s = np.abs(x-y)
# # plt.scatter(x,y,c=z,s=s)
# plt.show()

# sns.set(rc={"figure.figsize":(5,5)})
# sns.lineplot(x=[1,2,3,4],y=[1,4,9,16],
#              label='linia nr 1',color='red',
#              marker="o",linestyle=':')
# sns.lineplot(x=[1,2,3,4],y=[2,5,10,17],
#              label='linia nr 2',color='green',
#              marker="^",linestyle=':')
# plt.xlabel("oś x")
# plt.xticks([1,2,3,4])
# plt.ylabel("oś y")
# plt.show()
#

# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# sns.set()
# wykres = sns.relplot(kind="line",data=s,label="linia")
# wykres.fig.set_size_inches(8,6)
# wykres.fig.suptitle("Wykres liniowy losowych danych")
# wykres.set_xlabels("indeksy")
# wykres.set_ylabels("wartosci")
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=0.1,right=0.9,bottom=0.1,top=0.9)
# plt.show()

# sns.set()
# df = pd.read_csv('iris.csv',header=0, sep=',', decimal='.')
# wykres = sns.lineplot(data=df, x=df.index, y='sepal length',palette=['red','green','blue'], hue='class')
# wykres.set_xlabel("indeksy")
# wykres.set_title('XD')
# wykres.legend(title='Rodzaj')
# plt.show()

# sns.set()
# data ={'a': np.arange(10),
#        'c': np.random.randint(0,50,10),
#        'd': np.random.randn(10)}
# data['b'] = data['a']+10*np.random.randn(10)
# data['d'] = np.abs(data['d'])*100
# print(data['c'])
# print(data['d'])
# df = pd.DataFrame(data)
# plot = sns.relplot(data=df, x="a",y="b",
#                    hue="c", palette='bright',size='d', legend=True)
# plot.fig.set_size_inches(6,6)
# plot.set(xticks=data['a'])
# plt.show()

# dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Kontynent': ['Europa','Azja','Ameryka Południowa'],
#         'Populacja': [111908406, 130317135, 207847528]}
# df = pd.DataFrame(dane)
# sns.set()
# plot = sns.barplot(data=df, x="Kontynent", y="Populacja",
#                    ci=None, hue='Kontynent', estimator=np.sum,
#                    dodge=False, palette=['red','green','yellow'])
# plot.legend(title="Populacja na kontynent",loc="upper left")
# plot.set(title="Wykres słupkowy")
# plt.show()

ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel("Z label")
ax = fig.add_subplot(1,2,2,projection='3d')
X, Y, Z = get_test_data()
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
plt.show()
