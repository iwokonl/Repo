#zad_1 lab_2
sporty = ["bieganie","strzelanie","skakanie"]
sporty.reverse()
sporty.append("pływanie")
sporty.append("latanie")
print(sporty)

#zad_2 lab_2
skr = {'PZU': 'Państwowy zakład ubezpieczeń',
       'ZUS': 'Zakład ubespieczeń społecznych',
       'PKO': 'Państwowa kasa oszczędnośiowa',
       'WMiI': "Wydział matematyki i informatyki"}
print(skr)

#zad_3 lab_2


#zad_4 lab_2
a = input()
print(len(a))

#zad_5 lab_2
a = float(input())
b = float(input())
c = float(input())
wynik = a**b+c
print(wynik)

#zad_6 lab_2
pierwsza = float(input())
druga = float(input())
trzecia = float(input())
tab = [pierwsza,druga,trzecia]
najwieksza=pierwsza

for najwieksza in tab:
    if druga>najwieksza:
        najwieksza=druga
    if trzecia>najwieksza:
        najwieksza=trzecia
print(najwieksza)

#zad_7 lab_2
i=0
lista = [int(4),float(7.62)]
for x in lista:
    print(lista[i]**2)
    i += 1

# zad_8 lab_2
i=0
lista = []
while i<10:
    a = input()
    if float(a)%2==0:
        lista.append(a)
    i+=1
print(lista)

# zad_9 lab_2
import math

a = float(input())
if a>=0:
    print(math.sqrt(a))
else:
    print("Liczba musi być większa od 0")
