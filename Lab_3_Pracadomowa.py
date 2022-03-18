#Zad 1 .append()
import random

listaA = []
for x in range (1,11):
    listaA.append(1-x)
#print(listaA)

ListaB = []
for x in range (0,7):
    ListaB.append(pow(4,x))
#print(ListaB)

ListaC= []
for x in ListaB:
    if (x%2==0):
        ListaC.append(x)
#print(ListaC)
#Zad2
listaD = []
for x in range(0,10):
    listaD.append(random.randint(0,100))
#print(listaD)
listaD2 = []
for x in listaD:
    if (x % 2 ==0):
        listaD2.append(x)
#print(listaD2)

#zadanie3
produkty={'ser':"Kg", "Żelki":"Szt","Cola":"Szt"}
print(produkty)
lprodukty={key:value for key, value in produkty.items() if value=="Szt"}
print(lprodukty)

#zadanie4
def TrojProstokatny(a, b, c):
    if pow(a, 2)+pow(b, 2) == pow(c, 2):
        return 'tak'
    else:
        return 'Nie'
#zad5
def PoleTrapez(a=2,b=3,h=2):
    pole = ((a+b)*h/2)
    return pole
print(PoleTrapez())
#zad 6
def ciag(a =1,b =4, ile = 10):
    for x in range (ile):
        a = a * b
    return a
print(ciag())
#Zad 7
def ciag2(*liczba):
    z = 2
    for x in liczba:
        z = z * x
    return z

print(ciag2(1,2))
