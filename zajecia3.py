a = []
for x in range(0, 10):
    a.append(x**2)
a2 = [x**2 for x in range(0,10)]
print(a2)
b = []
for x in range(0,6):
        b.append(3**x)
        print(b)
b2=[3**x for x in range(0,6)]
print(b2)

c = []
for x in a:
    if x%2==1:
        c.append(x)
print(c)

d = [x for x in a if x%2==1]
print(d)

lista = []
for a in [1,2,3,]:
    for b in [4,5,6]:
        lista.append((a,b))
print(lista)
lista2 = [(a,b) for a in [1,2,3] for b in [4,5,6]]
print(lista2)

slownik = {'PZU': 'Państwowy zakład ubezpieczeń',
           'ZUS': 'Zakład ubespieczeń społecznych',
           'PKO': 'Państwowa kasa oszczędnośiowa'}
słownik_odwrócony = {}
for key,value in slownik.items():
    słownik_odwrócony[value]=key
    print(słownik_odwrócony)
slownik2 = {value: key for key, value in slownik.items()}
    print(slownik2)
import math
def delta(a,b,c):
    deltas = b**2-4*a*c
    if deltas<0:

        return "Brak rozwiązań"
    elif deltas==0:
        print("Jest jedno rozwiązanie")
        x = (-b)/(2*a)
        return x;
    else:
        print("Dwa rozwiązania")
        x1 = ((-b) - math.sqrt(deltas))/(2*a)
        x2 = ((-b) + math.sqrt(deltas)) / (2 * a)
        return x1 ,x2
print(delta(5,1,3))
print(delta(1,2,1))
print(delta(1,4,1))

def paz(a):
    if a%2==0:
        return "p"
    else:
        return "nie_p"
print(paz(3))
print(paz(22))

def dlugosc_odcinka(x1=1,y1=2,x2=3,y2=4):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
# ARG domyślne
print(dlugosc_odcinka())
# ARG pozycyjne
print(dlugosc_odcinka(4,8,222,183462))
print(dlugosc_odcinka(2,2,y2=7,x2=5))

def ciag(* liczby):
    if len(liczby)==0:
        return "Wynik=0"
    else:
        suma = 0
        for i in liczby:
            suma += i
        return suma
print(ciag())
print(ciag(1,2,3,4,5,6,7,8,9,10))

def co_lubie(** rzeczy):
    for cos in rzeczy:
        print("to jest ")
        print(cos)
        print("co lubie")
        print(rzeczy[cos])
co_lubie(gry=['planszowe',"komputerowe"])
