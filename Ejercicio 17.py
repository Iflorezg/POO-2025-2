import math

class Calculos:
    @staticmethod
    def ejercicio17(radio):
        area = math.pi * (radio ** 2)
        circunferencia = 2 * math.pi * radio
        return area, circunferencia


class Ejercicio17:
    def ejecutar(self):
        radio = float(input("Ingrese el radio del círculo: "))
        area, circunferencia = Calculos.ejercicio17(radio)
        print("Área:", area)
        print("Circunferencia:", circunferencia)


if __name__ == "__main__":
    Ejercicio17().ejecutar()
