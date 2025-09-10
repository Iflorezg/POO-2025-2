

import math
# Ejercicio Resuelto Nº 4
class Family:
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan
        self.edad_alberto = (2 / 3) * edad_juan
        self.edad_ana = (4 / 3) * edad_juan
        self.edad_mama = self.edad_juan + self.edad_alberto + self.edad_ana

    def mostrar_edades(self):
        print("=== Ejercicio Resuelto 4 ===")
        print(f"Juan: {self.edad_juan} años")
        print(f"Alberto: {self.edad_alberto} años")
        print(f"Ana: {self.edad_ana} años")
        print(f"Mamá: {self.edad_mama} años")
        print()

# Ejercicio Resuelto Nº 5
class Traza:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ejecutar(self):
        print("=== Ejercicio Resuelto 5 ===")
        print(f"Valores iniciales: a={self.a}, b={self.b}")
        self.a = self.a + 2
        print(f"Después de a=a+2: a={self.a}, b={self.b}")
        self.b = self.a - self.b
        print(f"Después de b=a-b: a={self.a}, b={self.b}")
        self.a = self.a * self.b
        print(f"Después de a=a*b: a={self.a}, b={self.b}")
        print()


# Ejercicio Propuesto Nº 12
class Empleado:
    def __init__(self, horas_trabajadas, valor_hora, porcentaje_retencion):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion

    def calcular_pago(self):
        bruto = self.horas_trabajadas * self.valor_hora
        retencion = bruto * self.porcentaje_retencion
        neto = bruto - retencion
        print("=== Ejercicio Propuesto 12 ===")
        print(f"Sueldo bruto: {bruto}")
        print(f"Retención: {retencion}")
        print(f"Sueldo neto: {neto}")
        print()


# Ejercicio Propuesto Nº 14
class Potencias:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        cuadrado = self.numero ** 2
        cubo = self.numero ** 3
        print("=== Ejercicio Propuesto 14 ===")
        print(f"Número: {self.numero}")
        print(f"Cuadrado: {cuadrado}")
        print(f"Cubo: {cubo}")
        print()


# Ejercicio Propuesto Nº 17
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular(self):
        area = math.pi * (self.radio ** 2)
        circunferencia = 2 * math.pi * self.radio
        print("=== Ejercicio Propuesto 17 ===")
        print(f"Radio: {self.radio}")
        print(f"Área: {area}")
        print(f"Circunferencia: {circunferencia}")
        print()


# Programa principal

if __name__ == "__main__":
    # Ejercicio 4
    familia = Family(9)  # Juan tiene 9 años
    familia.mostrar_edades()

    # Ejercicio 5
    traza = Traza(5, 3)
    traza.ejecutar()

    # Ejercicio 12
    empleado = Empleado(48, 5000, 0.125)
    empleado.calcular_pago()

    # Ejercicio 14
    pot = Potencias(3)
    pot.calcular()

    # Ejercicio 17
    c = Circulo(5)
    c.calcular()

