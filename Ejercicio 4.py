class Calculos:
    @staticmethod
    def ejercicio4(juan):
        alberto = (2/3) * juan
        ana = (4/3) * juan
        mama = juan + alberto + ana
        return alberto, ana, mama


class Ejercicio4:
    def ejecutar(self):
        juan = float(input("Ingrese la edad de Juan: "))
        alberto, ana, mama = Calculos.ejercicio4(juan)
        print("Alberto:", alberto)
        print("Ana:", ana)
        print("Mamá:", mama)


if __name__ == "__main__":
    Ejercicio4().ejecutar()
