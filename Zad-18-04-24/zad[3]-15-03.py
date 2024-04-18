class Kot:


    def __init__(self, imie=None):

        self.imie = imie

    def set_name(self, imie):

        self.imie = imie

    def get_name(self):
 
        return self.imie

def main():
    # Przykład użycia
    kot1 = Kot()  # Kot bez imienia
    kot2 = Kot("Mruczek")  # Kot z imieniem "Mruczek"

    print(f"Kot 1: {kot1.get_name()}")  # Wyświetli "None"
    print(f"Kot 2: {kot2.get_name()}")  # Wyświetli "Mruczek"

    kot1.set_name("Puszek")  # Ustaw imię kota 1 na "Puszek"
    print(f"Kot 1: {kot1.get_name()}")  # Wyświetli "Puszek"

if __name__ == "__main__":
    main()
