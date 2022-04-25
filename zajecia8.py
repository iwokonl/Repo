import numpy as np

a = np.array([20, 30, 40, 50])
b = a
c = a + b
print(c)
print(b**2)

print(np.exp(b))
print(np.sqrt(b))
d = np.sqrt(b)
e = d + b
print(e)

a = np.arange(12).reshape((3, 4))
print(a)
print(a.sum())
print(a.sum(axis=0)) # suma dla każdej z kolumn
print(a.sum(axis=1)) # suma dla każdego z wierszy
print(a.cumsum(axis=1)) # suma wszystkih elementów wiersza do danej pozycji

a = np.arange(3)
b = np.arange(3)
print(a.dot(b))

c = np.array([[2, 3, 6], [5, 1, 3]])
d = np.array([[1, 4], [2, 1], [3, 5]])
e = c.dot(d)
print(e)

a = np.arange(6).reshape(3, 2)
print(a)
# for b in a:
#     for c in b:
#         print(c)
for b in a.flat:
    print(b)

a = np.arange(6)
print(a)
b = a.reshape((3, 2))
c = a.reshape((2, 3))
print(b)
print(c)
d = c.ravel()
print(d)
e = c.T
print(e)
