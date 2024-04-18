import random

def losuj_liczby(n, min, max):

  return [random.randint(min, max) for _ in range(n)]

def najdluzsze_podciagi_rosnace(liczby):

  n = len(liczby)
  dlugosci = [1] * n
  poprzednie = [None] * n

  for i in range(1, n):
    for j in range(i):
      if liczby[i] >= liczby[j] and dlugosci[i] < dlugosci[j] + 1:
        dlugosci[i] = dlugosci[j] + 1
        poprzednie[i] = j

  max_dlugosc = max(dlugosci)
  podroze = []
  i = n - 1
  while i is not None and max_dlugosc > 0:
    podroz = []
    while i is not None and max_dlugosc > 0:
      podroz.append(liczby[i])
      i = poprzednie[i]
      max_dlugosc -= 1
    podroz.reverse()
    podroze.append(podroz)

  return podroze

def main():
  # Przykładowe wywołanie funkcji
  liczby = losuj_liczby(10, 0, 20)
  print(f"Lista liczb: {liczby}")

  naj_dluzsze_podciagi = najdluzsze_podciagi_rosnace(liczby)
  print(f"Najdłuższe spójne podciągi rosnące:")
  for podciag in naj_dluzsze_podciagi:
    print(f"  - {podciag}")

if __name__ == "__main__":
  main()