class Calculos:
    @staticmethod
    def ejercicio5_suma(suma, x):
        return suma + x

    @staticmethod
    def ejercicio5_x(x, y):
        return x + (y ** 2)


class Ejercicio5:
    def ejecutar(self):
        suma = float(input("Ingrese un número para suma: "))
        x = float(input("Ingrese un número para x: "))
        y = float(input("Ingrese un número para y: "))
        suma = Calculos.ejercicio5_suma(suma, x)
        x = Calculos.ejercicio5_x(x, y)
        suma = suma + (x / y)
        print("El valor de la suma es:", suma)


if __name__ == "__main__":
    Ejercicio5().ejecutar()
