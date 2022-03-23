a = 3
b = 7
if a > b:
    print('liczba a jest większa od b')
elif b > a:
    print('liczba a jest większa od b')
else:
    print('są sobie równe')
if a==b:
    print('A jest równe B')
else:
    print('Nie są sobie równe')

a =input('podaj liczbe:')
a=int(a)
print(a)
print(type(a))

a = int(input('podaj a liczbe:'))
b = int(input('podaj b liczbe:'))
c = int(input('podaj c liczbe:'))
d = int(input('podaj d liczbe:'))
if (a>b) & (c>d):
    print("a jest większe od b i c jest większe od d")
else:
    print("podany warunek nie zachodzi")

for a in range(0,7,1):
    print(a)

lista = ['cos', 5, 4, 6.5]
for a in lista:
    print(a)
else:
    print("Wyświetlono wszystkie elementy z lista")
licznik = 0
while licznik!=11:
    print(licznik)
    licznik+=1

lista = [8,4,2,3,1,88]
licznik=0
liczba=input("wpisz liczbę całkowitą:")
while licznik!=len(lista):
    if int(liczba) - lista[licznik] == 0:
        print('liczba ' + str(liczba) + "-" + str(lista[licznik]) + "=0")
        break
    else:
        licznik += 1
else:
    print("Żadna z wartości nie dała odpowiedniego wyniku")

lista1 = [1,2,3,4,5,6,7,8]
lista2 = [3,4,5,6,7]
suma = []
for a in lista1:
    for b in lista2:
        wynik=a+b
        suma.append(wynik)
    print(suma)
a = input("padaj pierwszą:")
b = input("podaj drugą:")
try:
    a = int(a)
    b = int(b)
    wynik= a/b
    print(wynik)
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Wpisz liczbę całkowitą")

my_dict = {'name': 'Iwo', 'age': 21, 1:2}
print(my_dict)
my_dict["XD"] = "XD"
my_dict["height"] = [4]
my_dict['height'].append(180)
my_dict.insert(13)
print(my_dict)

