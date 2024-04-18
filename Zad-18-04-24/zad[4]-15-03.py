class Rower:
    """Klasa reprezentująca rower."""

    def __init__(self, kolor, vMax=20):

        self.kolor = kolor
        self.vMax = vMax
        print(f"Utworzono nowy rower o kolorze {self.kolor}.")

    def set_vMax(self, nowa_vMax):
   
        if nowa_vMax < 0:
            raise ValueError("Maksymalna prędkość nie może być ujemna!")
        self.vMax = nowa_vMax
        print(f"Zmieniono maksymalną prędkość roweru do {self.vMax} km/h.")

    def __del__(self):
        """Destruktor roweru. Wyświetla komunikat o usunięciu."""
        print(f"Usunięto rower o kolorze {self.kolor}.")

def main():
    # Przykład użycia
    rower1 = Rower("niebieski")
    rower1.set_vMax(30)

    rower2 = Rower("czerwony", 45)

    # Usunięcie rowerów
    del rower1
    del rower2

if __name__ == "__main__":
    main()
