class Calculos:
    @staticmethod
    def ejercicio14(numero):
        return numero ** 2, numero ** 3


class Ejercicio14:
    def ejecutar(self):
        numero = float(input("Ingrese un número: "))
        cuadrado, cubo = Calculos.ejercicio14(numero)
        print("Cuadrado:", cuadrado)
        print("Cubo:", cubo)


if __name__ == "__main__":
    Ejercicio14().ejecutar()
