def policz_podciagi_o_sumie(liczby, suma):

  n = len(liczby)
  prefiksowe_sumy = [0] * n
  prefiksowe_sumy[0] = liczby[0]
  liczba_podciagow = 0

  # Zbudowanie tablicy prefiksowych sum
  for i in range(1, n):
    prefiksowe_sumy[i] = prefiksowe_sumy[i-1] + liczby[i]

  # Zliczanie podciągów dla każdej wartości prefiksowej sumy
  for i in range(n):
    # Znajdź początkowe indeksy podciągów o sumie "suma"
    lewy = bisect_left(prefiksowe_sumy, i + suma)
    prawy = bisect_right(prefiksowe_sumy, i + suma)

    # Zlicz podciągi, biorąc pod uwagę podciągi z prawej strony
    liczba_podciagow += prawy - lewy

    # Zastosuj korekcję dla przypadku, gdy suma jest równa prefiksowej sumie
    if prefiksowe_sumy[i] == suma:
      liczba_podciagow -= 1

  return liczba_podciagow

def main():
  # Wczytaj dane
  n = int(input("Podaj liczbę elementów: "))
  suma = int(input("Podaj sumę, dla której chcesz znaleźć podciągi: "))

  # Wczytaj liczby
  liczby = [int(liczba) for liczba in input("Podaj liczby oddzielone spacjami: ").split()]

  # Wylicz liczbę podciągów
  liczba_podciagow = policz_podciagi_o_sumie(liczby, suma)

  # Wyświetl wynik
  print(f"Liczba podciągów spójnych o sumie {suma}: {liczba_podciagow}")

if __name__ == "__main__":
  main()
