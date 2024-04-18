def maksymalna_suma_podciagu(liczby):

  n = len(liczby)
  suma_do_tej_pozycji = [0] * n
  maksymalna_suma = liczby[0]

  # Przejście w prawo (od lewej do prawej)
  for i in range(n):
    suma_do_tej_pozycji[i] = max(liczby[i], suma_do_tej_pozycji[i-1] + liczby[i])
    maksymalna_suma = max(maksymalna_suma, suma_do_tej_pozycji[i])

  # Przejście w lewo (od prawej do lewej)
  suma_do_tej_pozycji = [0] * n
  maksymalna_suma_do_tej_pozycji = liczby[n-1]

  for i in range(n-2, -1, -1):
    suma_do_tej_pozycji[i] = max(liczby[i], suma_do_tej_pozycji[i+1] + liczby[i])
    maksymalna_suma_do_tej_pozycji = max(maksymalna_suma_do_tej_pozycji, suma_do_tej_pozycji[i])

  # Znajdź maksymalny podciąg uwzględniając oba przejścia
  maksymalna_suma_podciagu = maksymalna_suma
  for i in range(n):
    maksymalna_suma_podciagu = max(maksymalna_suma_podciagu, suma_do_tej_pozycji[i] + suma_do_tej_pozycji[i-1] - liczby[i])

  return maksymalna_suma_podciagu

def main():
  # Przykładowe wywołanie funkcji
  liczby = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  print(f"Lista liczb: {liczby}")

  maksymalna_suma = maksymalna_suma_podciagu(liczby)
  print(f"Maksymalna suma podciągu: {maksymalna_suma}")

if __name__ == "__main__":
  main()
