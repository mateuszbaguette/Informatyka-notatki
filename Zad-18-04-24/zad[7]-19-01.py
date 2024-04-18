def znajdz_podciagi_o_sumie(liczby, suma):

  n = len(liczby)
  prefiksowe_sumy = [0] * n
  prefiksowe_sumy[0] = liczby[0]
  podroze = []

  # Zbudowanie tablicy prefiksowych sum
  for i in range(1, n):
    prefiksowe_sumy[i] = prefiksowe_sumy[i-1] + liczby[i]

  # Znajdowanie podciągów
  def znajdz_podciagi(i, suma_do_tej_pozycji, podroz):
    if i == n:
      if suma_do_tej_pozycji == suma:
        podroze.append(podroz.copy())
      return

    if suma_do_tej_pozycji > suma:
      return

    # Dodanie bieżącego elementu do podciągu
    podroz.append(liczby[i])
    znajdz_podciagi(i + 1, suma_do_tej_pozycji + liczby[i], podroz)

    # Usunięcie bieżącego elementu z podciągu (backtracking)
    podroz.pop()
    znajdz_podciagi(i + 1, suma_do_tej_pozycji, podroz)

  znajdz_podciagi(0, 0, [])
  return podroze

def main():
  # Wczytaj dane
  n = int(input("Podaj liczbę elementów: "))
  suma = int(input("Podaj sumę, dla której chcesz znaleźć podciągi: "))

  # Wczytaj liczby
  liczby = [int(liczba) for liczba in input("Podaj liczby oddzielone spacjami: ").split()]

  # Znajdź podciągi
  podroze = znajdz_podciagi_o_sumie(liczby, suma)

  # Wyświetl wynik
  if podroze:
    print("Znalezione podciągi:")
    for podroz in podroze:
      print(podroz)
  else:
    print("Nie znaleziono podciągów o podanej sumie.")

if __name__ == "__main__":
  main()
