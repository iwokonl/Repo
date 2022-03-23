class Kształty():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = "To jest klasa dla ogólnych kształtów"

    def pole(self):
        return self.x*self.y

    def obwod(self):
        return 2*self.x+2*self.y

    def dodaj_opis(self,text):
        self.opis=text

    def skalowanie(self,czynnik):
        self.x=self.x*czynnik
        self.y=self.y*czynnik

class kwadrat(Kształty):
    def __init__(self,x):
        self.x=x
        self.y=x

class kwadrat_L(kwadrat):
    def obw(self):
        return 8*self.x
    def pole(self):
        return 3*self.x*self.y

Kwadrat = kwadrat(5)
print(Kwadrat.obwod())
print(Kwadrat.pole())
Kwadrat.dodaj_opis("Nasza figura")
print(Kwadrat.opis)
Kwadrat.skalowanie(0.3)
print(Kwadrat.obwod())
print("")
litera_l = kwadrat_L(5)
print(litera_l.obwod())
print(litera_l.pole())
litera_l.dodaj_opis("Litera L")
print(litera_l.opis)
litera_l.skalowanie(0.5)
print(litera_l.obwod())


class Kwadrat(Kształty):
    def __init__(self, x):
        self.x=x
        self.y=x

    def __str__(self):
        return "kwadrat o boku {}".format(self.x)

kwadrat = Kwadrat(5)
print(kwadrat)


class Osoba:
    def __init__(self,imie,nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class pracownik(Osoba):
    def __init__(self,imie,nazwisko,pensja):
        Osoba.__init__(self,imie,nazwisko)
        self.pensja=pensja
    def przedstaw_sie(self):
        return "{} {} jestem robolem i zarabiam {}".format(self.imie,self.nazwisko,self.pensja)

class menager(pracownik):
    def przedstaw_sie(self):
        return "{} {} jestem menadzerem i zarabiam {}".format(self.imie,self.nazwisko,self.pensja)

jozek=pracownik("Józef","Beka",2137)
Franek=menager("Franisław","Beczkowy",213700)

print(jozek.przedstaw_sie())
print(Franek.przedstaw_sie())
imie = "reks"
it =iter(imie)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
