from math import *
print("[Zadanie 1]")
liczba = int(input("wpisz liczbe calkowita"))
if liczba % 2 == 0:
  print("parzysta")
else:
  print("nie parzysta")


print("[Zadanie 2]")

a = int(input("1 liczba"))
b = int(input("2 liczba"))
c = int(input("3 liczba"))

maks = a
if b > maks:
    maks = b
if c > maks:
     maks = c
print("Najwieksza liczba to:", maks)

print("[Zadanie 3]")

def funkcja(x):
  if x < 1:
    return 2*x
  else:
    if x == 3:
      return x**4
    else:
      if x == 6:
        return sqrt(x-4)
      else:
        return 0
print(funkcja(-8))
print(funkcja(3))
print(funkcja(6))
print(funkcja(59))

print("[Zadanie 4]")

a = float(input("Pierwszy odcinek: "))
b = float(input("Drugi odcinek: "))
c = float(input("Trzeci odcinek: "))

def trojkat(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    return True
  else:
    return False

if trojkat(a, b, c):
    print("Mozesz utworzyc trojkat")
else:
    print("Nie mozesz utworzyc trojkota")

print("[Zadanie 5]")


a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))

def p_trojkata(a, b, c):
    p = (a + b + c) / 2
    pierwiastek = p * (p - a) * (p - b) * (p - c)
    if pierwiastek >= 0:
        pole = sqrt(pierwiastek)
        return pole
    else:
        return "blad, liczba pod pierwiaskiem jest ujemna"

wynik = p_trojkata(a, b, c)
print("Pole wynosi:", wynik)

