import random

def losuj_liczby(n, min, max):
 
  return [random.randint(min, max) for _ in range(n)]

def najdluzszy_podciag_rosnacy(liczby):

  n = len(liczby)
  dlugosci = [1] * n
  poprzednie = [None] * n

  for i in range(1, n):
    for j in range(i):
      if liczby[i] >= liczby[j] and dlugosci[i] < dlugosci[j] + 1:
        dlugosci[i] = dlugosci[j] + 1
        poprzednie[i] = j

  max_dlugosc = max(dlugosci)
  naj_dluzszy_podciag = []
  i = n - 1
  while i is not None and max_dlugosc > 0:
    naj_dluzszy_podciag.append(liczby[i])
    # Sprawdź i przed odwołaniem się do poprzednie[i]
    if i is not None:  
      i = poprzednie[i]
    max_dlugosc -= 1

  naj_dluzszy_podciag.reverse()
  return naj_dluzszy_podciag


def main():
  # Przykładowe wywołanie funkcji
  liczby = losuj_liczby(10, 0, 20)
  print(f"Lista liczb: {liczby}")

  naj_dluzszy_podciag = najdluzszy_podciag_rosnacy(liczby)
  print(f"Najdłuższy spójny podciąg rosnący: {naj_dluzszy_podciag}")

if __name__ == "__main__":
  main()