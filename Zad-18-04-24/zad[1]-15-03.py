import math

class FunkcjaKwadratowa:


  def __init__(self, a, b, c):
    """
    Konstruktor klasy FunkcjaKwadratowa.

    Args:
      a: Współczynnik przy x^2.
      b: Współczynnik przy x.
      c: Wyraz wolny.
    """
    self.a = a
    self.b = b
    self.c = c

  def Rozwiaz(self):
  
    if self.a == 0:
      # Przypadek a = 0
      if self.b == 0:
        # Przypadek a = b = 0
        return None  # Nieskończona liczba rozwiązań
      else:
        x = -self.c / self.b
        return (x, x)  # Jeden pierwiastek podwójny
    else:
      delta = self.b**2 - 4 * self.a * self.c
      if delta < 0:
        return "Brak rozwiązań rzeczywistych"  # Brak pierwiastków rzeczywistych
      else:
        pierwiastek1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
        pierwiastek2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
        return (pierwiastek1, pierwiastek2)  # Dwa pierwiastki

def main():
  # Przykład użycia
  f = FunkcjaKwadratowa(1, 2, -3)
  pierwiastki = f.Rozwiaz()

  if pierwiastki is None:
    print("Funkcja ma nieskończenie wiele rozwiązań.")
  elif isinstance(pierwiastki, str):
    print(pierwiastki)  # Wyświetl komunikat o braku rozwiązań
  else:
    print(f"Pierwiastki funkcji to: x1 = {pierwiastki[0]}, x2 = {pierwiastki[1]}")

if __name__ == "__main__":
  main()
