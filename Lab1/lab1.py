# zad1
x = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print("-----------------")
# zad2
imie = "Patryk"
nazw = "Jurczyk"
litera_1 = imie[1]
litera_2 = nazw[2]
d = len(x)
liczba_liter1 = 0
liczba_liter2 = 0
for i in range(d):
    if litera_1 == x[i]:
        liczba_liter1 = liczba_liter1+1
    elif litera_2 == x[i]:
        liczba_liter2 = liczba_liter2+1
print("W teście jest ", liczba_liter1, " liter ", litera_1," oraz ", liczba_liter2, " liter ", litera_2)
# zad3
print("{:d} dalmatyńczyków".format(101))
urodziny = {'dzień': 'pierwszy', 'miesiąc': 'styczeń'}
print('{dzień} {miesiąc}'.format(**urodziny))
print('{dzień} {miesiąc}'.format(dzień='drugi', miesiąc='luty'))
data = [1,2,3,4,5,6,7,8,9,0]
print('{d[4]} {d[2]}'.format(d=data))
class Planet(object):
    type = 'ziemia'
print('{p.type}'.format(p=Planet()))
print("-----------------")
# zad4

zmienna_typu_string = "W ostatnim czasie w mediach, obok epidemiologów, brylują specjaliści od pracy zdalnej. Dziesiątki coachów udziela rad typu: „jak pracować w domu, żeby nie zwariować”. Każdy, kto na dobre zasmakował telepracy, patrzy na takie wskazówki z przymrużeniem oka. Może nie zaszkodzą, ale też niewiele pomogą."

print(dir(zmienna_typu_string))
help(zmienna_typu_string.count("W"))
print("-----------------")

# zad5
print(imie[::-1], nazw[::-1])
print("-----------------")

# zad6
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_x = []
for i in range(len(x)+1):
    if i > len(x)/2:
        new_x.append(i)
del x[len(x)//2:x[len(x)-1]]
print(x)
print(new_x)
print("-----------------")

# zad7
for i in range(len(new_x)):
    x.append(new_x[i])
x.insert(0, 0)
copy_x = x
copy_x.reverse()
print(copy_x)
print("-----------------")

# zad8
krotkowa_lista = ("Andrzej Iksiński", 123456, "Paweł Kowalski", 456789, "Eryk Krygier", 158326)
print(krotkowa_lista)
print("-----------------")

# zad9
slownik = {
    "Andrzej Iksiński": "123456",
    "wiek A": "20",
    "adres A": "Krakowska 27",
    "email A": "kochampsy@gmail.com",
    "rok urodzenia A": "2001",
    "Paweł Kowalski": "456789",
    "wiek P": "22",
    "adres P": "Marcepanowa 27",
    "email P": "kochamkoty@gmail.com",
    "rok urodzenia P": "1999",
    "Eryk Krygier": "158326",
    "wiek M": "21",
    "adres M": "Arkadia 27",
    "rok urodzenia M": "2000",
}
print(slownik)
print("-----------------")

# zad 10
tel_num = [123456789, 123456789, 111555999, 111555888]
print(set(tel_num))
print("-----------------")

# zad 11
for i in range(1, 10):
    print(i)
print("-----------------")

# zad 12
for i in range(0, 121):
    if i%5 == 0:
        print(100-i)
print("-----------------")

# zad 13

slownik1 = {
    "Grzegorz Kowalski": "123456",
    "wiekG": "22",
    "adresG": "Olkuska 27",
    "emailG": "mygmail@gmail.com",
    "rok urodzeniaG": "1999"
}
slownik2 = {
    "Franek Kimono": "789101",
    "wiekF": "22",
    "adresF": "Olkuska 26",
    "emailF": "mygmail@gmail.com",
    "rok urodzeniaF": "1999"
}
slownik3 = {
    "Patryk Jurczyk": "123113",
    "wiekP": "21",
    "adresP": "Boska 1",
    "emailF": "mygmail@gmail.com",
    "rok urodzeniaP": "2000"
}

tab13 = [slownik1, slownik2, slownik3]

pom = 0
while(pom < len(tab13)):
    for key in tab13[pom]:
        t = tab13[pom]
        print(key, " : ", t[key])
    pom = pom + 1