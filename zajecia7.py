import numpy as np
# a = np.arange(2)
# print(a)

# # inicjalizacja tablicy 1. sposob
# a = np.array([0, 1])
# print(a)
# # inicjalizacja tablicy 2. sposob
# a = np.arange(2)
# print(a)

# # wypisanie typu zmiennej tablicy (nie jej elementów) - ndarray
# print(type(a))
# # sprawdzenie typu tablicy
# print(a.dtype)

# # inicjalizacja tablicy z konkretnym typem danych
# a = np.arange(2, dtype = 'int64')
# print(a.dtype)
# # zapisanie kopii tablicy jako tablicy z innym typem
# b = a.astype('float')
# print(b)
# print(b.dtype)
#
# # wypisanie rozmiaru tablicy
# print(b.shape)
# # sprawdzenie ilości wymiarów tablicy
# print(a.ndim)


# # TABLICA WIELOWYMIAROWA
# # parametrem przekazywanym do funkcji array jest obiekt, który zostanie skonwertowany na tablicę
# # takim obiektem może być pythonowa lista
# m = np.array([np.arange(2), np.arange(2)])
# print(m)
# print(m.shape)
# # typem tablicy znowu jest ndarray
# print(type(m))


# # MACIERZ
# # łatwy sposób stworzenia macierzy danego rozmiaru wypełnionej zerami lub jedynkami
# zera = np.zeros((5, 5))
# jedynki= np.ones((4, 3))
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)
# # stworzenie pustej macierzy, która wcale nie jest pusta
# # umieszczane wartości sa losowe
# # najpierw podawana jest ilosc wierszy tablicy, potem ilosc kolumn
# pusta = np.empty((2, 2))
# print(pusta)
# # do elementów tablicyc możemy odwołac się tak jak do elementów np. listy czyli podając indeksy
# poz_1 = pusta[1, 1]
# poz_2 = pusta[0, 1]
# print(poz_1)
# print(poz_2)
# # tworzenie macierzy 2x2 wraz z uzupenieniem
# macierz = np.array([[1, 2], [3, 4]])
# print(macierz)
# # możemy utworzyć dwie macierze, najpierw wartości interowane są w kolumnie a następnie w wierszu
# z = np.indices((5, 3))
# print(z)
# # wielowymiarowe macierze możemy również generować funkcja mgrid
# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)
# # podobnie jak w MATLAB-ie możemy tworzyć macierze diagonalne
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
# # w powyższym przykładzie stworzony wektor wartości zostanie umieszczony na  głównej przekątnej macierzy
# # możemy podać drugi parametr funkcji diag, który okresla indeks przekątnej względem głównej przekątnej
# # zostanie ona wypełniona wartosciami podanego wektora
# mat_diag_k = np.diag([a for a in range(5)], -1)
# print(mat_diag_k)


# # funkcja arange potrafi także tworzyć ciągi liczb zmienno przecinkowych
# liczby = np.arange(1, 2, 0.1)
# print(liczby)
# # podobnie działa funkcja linspace, której działanie jest równoważne tej samej funkcji w MATLAB-ie
# liczby_lin = np.linspace(1, 2, 5) # pierwsze dwie liczby odkąd dokąd, ostatnia dzieli przedział na daną liczbę części
# print(liczby_lin)
# # Numpy jest wstanie stworzyć tablicę jednowymiarową z dowolnego obiektu iterowalnego (iterable)
# z = np.fromiter(range(5), dtype='int32')
# print(z)
# # ciekawą funkcją Numpy jest funkcja frombuffer, dzięki której możemy stworzyć np. tablicę znaków
# marcin = b'Marcin'
# # mar = np.frombuffer(marcin, dtype='S1')
# # print(mar)
# # mar_2 = np.frombuffer(marcin, dtype='S2')
# # print(mar_2)
# # powyższa funckja ma jednak pewna wadę dla pythona 3.x,
# # trzeba jawnie określić, że ciąg znaków przekazujemy jako ciąg bajtów
# # osiągamy to poprzez podanie litery 'b' przed wartością zmiennej tekstowej
# # podobne efekty można osiągnac inaczej
# marcin = 'Marcin'
# mar_3 = np.array(list(marcin))
# mar_4 = np.array(list(marcin), dtype='S1')
# mar_5 = np.array(list(b'Marcin'))
# mar_6 = np.fromiter(marcin, dtype='S1')
# mar_7 = np.fromiter(marcin, dtype='U1')
# print(mar_3)
# print(mar_4)
# print(mar_5)
# print(mar_6)
# print(mar_7)

# # tablice w Numpy możemy w prosty sposób do siebie dodawać, odejmowac, mnożyć, dzielić
# mat = np.ones((2, 2))
# mat_1 = np.ones((2, 2))
# mat = mat + mat_1
# print(mat)
# print(mat - mat_1)
# print(mat * mat_1)
# print(mat / mat_1)


# # INDEKSOWANIE I CIĘCIA TABLIC
# # cięcie (slicing) tablicy numpy mozna wykonać za pomoca wartości funckji slice lub range
# a = np.arange(10)
# print(a)
# s = slice(2, 7, 2)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])
# # mozemy ciąc tablice równiez w sposób znany z cięcia list
# print(a[2:7:2])
# print(a[1:])
# print(a[2:5])
# # w podobny sposób postępujemy w przypadku tablic wielowymiarowych
# mat = np.arange(25)
# print(mat)
# # teraz zmieniamy kształt tablicy jednowymiarowej na macierz 5x5
# mat = mat.reshape((5, 5))
# print(mat)
# print(mat[1:])  # od drugiego wiersza
# print(mat[:, 1])  # druga kolumna jako wektor
# print(mat[:, -1:])  # ostatnia kolumna
# print(mat[2:6, 1:3])  # 2 i 3 kolumna dla 3, 4, 5 wierszy
# print(mat[:, range(2, 6, 2)])  # 3 i 5 kolumna
# print('')
# bardziej zaawansowane, lecz trudniejsze do zrozumienia cięcia można osiągnąc tak jak poniżej:
# y będzie tablicą zawierającą wierzchołki macierzy x
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])  # bierze pierwsze wspolrzedne (wiersze) wierzchołków
print(rows)
cols = np.array([[0, 2], [0, 2]])  # bierze drugie wspolrzedne (kolumny) wierzchołków
print(cols)
y = x[rows, cols]  # łączy te współrzędne w punkty i wybiera liczby z x które na nich są
print(y)
