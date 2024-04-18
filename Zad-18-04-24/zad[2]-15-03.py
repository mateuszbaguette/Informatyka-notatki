import cmath

class Zespolona:


    def __init__(self, re, im):
     
        self.re = re
        self.im = im

    def __str__(self):
      
        if self.im >= 0:
            return f"{self.re:.2f} + {self.im:.2f}i"
        else:
            return f"{self.re:.2f} - {abs(self.im):.2f}i"

    def modul(self):
     
        return abs(complex(self.re, self.im))

    @staticmethod
    def dodaj(liczba1, liczba2):
       
        return Zespolona(liczba1.re + liczba2.re, liczba1.im + liczba2.im)

    @staticmethod
    def mnoz(liczba1, liczba2):
      
        return Zespolona(liczba1.re * liczba2.re - liczba1.im * liczba2.im,
                         liczba1.re * liczba2.im + liczba1.im * liczba2.re)

def main():
    # Przykład użycia
    liczba1 = Zespolona(2, 3)
    liczba2 = Zespolona(4, -5)

    print(f"Liczba 1: {liczba1}")
    print(f"Liczba 2: {liczba2}")

    suma = Zespolona.dodaj(liczba1, liczba2)
    iloczyn = Zespolona.mnoz(liczba1, liczba2)

    print(f"Suma: {suma}")
    print(f"Iloczyn: {iloczyn}")

if __name__ == "__main__":
    main()
