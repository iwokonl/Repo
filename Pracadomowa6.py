import numpy as np

a = np.arange(0,20*4+1,4)
print(a)
print("Zad 1")
a = np.array([1,2,3,4],dtype='float64')
print(a)

print("Zad 3")
print(a.dtype)
b = a.astype('int64')
print(b.dtype)
print(b)

print("Zad 4")
n = 5
a = np.arange(1,n**2+1)
b = a.reshape(n,n)
print(b)

print("Zad 5")
def generuj(n, z):
    a = np.logspace(1, z, num=z, base=n, dtype=int)
    return a
print(generuj(2,4))

print("Zad 6")
n = 4
a = np.arange(n)
a = np.flip(a)
a = np.diag(a,-2)
print


print("zad 7")
def foo(n):
    temp = np.eye(n) * 2
    for i in range(1, n):
        temp += np.eye(n, k=i) * 2 * (i + 1)
        temp += np.eye(n, k=-i) * 2 * (i + 1)
    return temp
print(foo(7))

print("Zad 8")
kierunek = 0
a = np.array([np.arange(4),np.arange(4)])
print(a)

print("zad 9")
z = 25
a = np.arange(z)
i = 0
for x in range(0,z):
     a[i] = 3+(x)*5
     i = i + 1
a = np.resize(a,(5,5))
print(a)
