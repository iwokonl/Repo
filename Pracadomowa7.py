import numpy as np

print("Zad 1")
a = np.arange(3)
a = b = np.reshape(a,(1,3))
print(a*b)

print("Zad 2")
a = np.arange(9)
b = np.arange(16)
a = np.reshape(a,(3,3))
b = np.reshape(b,(4,4))
print(a)
print()
print(b)
print()
print(a.min(axis=1))
print(b.min(axis=0))
print(b.min(axis=1))
print(b.min(axis=0))

print("Zad 4")
a = np.arange(3).reshape((1,3))
b = np.array([2.5,65.2,45.2]).reshape((1,3))
print(a*b)

print("Zad 5")
a = np.arange(6).reshape((2,3))
a = np.sin(a)
print(b)

print("Zad 6")
b = np.arange(6).reshape((2,3))
b = np.cos(a)
print(b)

print("Zad 7")
def dodawanie():
    return a+b
print(dodawanie())

print("Zad 8")
a = np.arange(9).reshape((3,3))
print(a.T)
for i in a.T:
    print(i)

print("Zad 9")
a = np.arange(9).reshape((3,3))
print(a)
for i in a.flat:
    print(i)
    print()

print("Zad 10")

a = np.arange(81).reshape((9,9))
print(a)
m1 = a.reshape((3,27))
m2 = a.reshape((1,81))
print(m1)
print(m2)

print("Zad 11")
a = np.arange(12).reshape((3,4))
b = np.reshape(a,(4,3))
c = np.reshape(a,(2,6))
print(a)
print()
print(b)
print()
print(c)
