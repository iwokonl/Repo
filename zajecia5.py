# # Dziedziczenie
# # Klasa główna (superklasa)
# class Ksztalty():
#     # definicja konstruktora
#     def __init__(self, x, y):
#         # deklarancja atrybutów
#         # self mówi, że chodzi o zmienne właśnie definiowanej klasy
#         self.x = x
#         self.y = y
#         self.opis = 'To jest klasa dla ogólnych kształtów'
#
#     def pole(self):
#         return self.x * self.y
#
#     def obwod(self):
#         return 2 * self.x + 2 * self.y
#
#     def dodaj_opis(self, tekst):
#         self.opis = tekst
#
#     def skalowanie (self, czynnik):
#         self.x = self.x * czynnik
#         self.y = self.y * czynnik
#
# # Klasa, która dziedzicy po klasie Ksztalty (podklasa)
# class Kwadrat(Ksztalty):
#     def __init__(self, x):
#         self.x = x
#         self.y = x
#
#     def __str__(self):
#         return 'Kwadrat o boku {}'.format(self.x)
#
# # Klasa, która dziedziczy po klasie Kwadrat
# # będzie definiować figurę złożoną z 3 kwadratów w kształcie litery L
# class KwadratLiteraL(Kwadrat):
#     def obwod(self):
#         return 8 * self.x
#
#     def pole(self):
#         return 3 * self.x * self.y
#
# # inicjacja klasy Kwadrat
# kwadrat = Kwadrat(5)
#
# # sprawdzenie metod z klasy bazowej
# print(kwadrat.obwod())
# print(kwadrat.pole())
# kwadrat.dodaj_opis('Ta figura to kwadrat')
# print(kwadrat.opis)
# kwadrat.skalowanie(0.3)
# print(kwadrat.obwod())
# print("")
#
# # inicjacja klasy KwadratLiteraL
# litera_l = KwadratLiteraL(5)
# print(litera_l.obwod())
# print(litera_l.pole())
# litera_l.dodaj_opis('Litera L')
# print(litera_l.opis)
# litera_l.skalowanie(0.5)
# print(litera_l.obwod())
# print("")
#
# print(kwadrat)
# print("")

# # Konstruktory klasy bazowej i dziedziczenie wielokrotne
# class Osoba:
#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#
#     def przedstaw_sie(self):
#         return 'Nazywam się {} {}'.format(self.imie, self.nazwisko)
#
# class Pracownik(Osoba):
#     def __init__(self, imie, nazwisko, pensja): # wywołanie kostruktora klasy bazowej
#         Osoba.__init__(self, imie, nazwisko)
#         #drugi sposób: super().__init__(imie, nazwisko)
#         self.pensja = pensja
#
#     def przedstaw_sie(self):
#         return 'Nazywam się {} {} i zarabiam {}'.format(self.imie, self.nazwisko, self.pensja)
#
# class Menadzer(Pracownik):
#     def przedstaw_sie(self):
#         return 'Nazywam się {} {}, jestem menadżerem i zarabiam {}'.format(self.imie, self.nazwisko, self.pensja)
#
# gerwazy = Pracownik('Gerwazy', 'Kąkuter', 2300)
# dezydery = Menadzer('Dezydery', 'Laptok', 11800)
#
# print(gerwazy.przedstaw_sie())
# print(dezydery.przedstaw_sie())
# print("")

# Iteratory i generatory
imie = 'Reks'
it = iter(imie)
print(it)
print("")

print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

# Implementacja własnego iteratora
class Wspak:
    def __init__(self, dane):
        self.dane = dane
        self.indeks = len(dane)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks == 0:
            raise StopIteration
        self.indeks -= 1
        return self.dane[self.indeks]

napis = Wspak('Reks')
print(napis.__next__())
for x in napis:
    print(x)
print("")

# przykład generatora
def na_odwrot(dane):
    for indeks in range(len(dane)-1, -1, -1):
        yield dane[indeks]

gen = na_odwrot("Remigiusz")
print(next(gen))
print("Mróz")
print(next(gen))
print("")

litery = (litera for litera in "Amadeusz")
print(litery)
print(next(litery))
