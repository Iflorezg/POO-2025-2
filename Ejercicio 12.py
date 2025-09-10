class Calculos:
    @staticmethod
    def ejercicio12(horas, valor_hora, porcentaje):
        bruto = horas * valor_hora
        retencion = bruto * porcentaje
        neto = bruto - retencion
        return bruto, retencion, neto


class Ejercicio12:
    def ejecutar(self):
        horas = float(input("Ingrese las horas trabajadas: "))
        valor_hora = float(input("Ingrese el valor de la hora: "))
        porcentaje = float(input("Ingrese el porcentaje de retención (ejemplo 0.125): "))
        bruto, retencion, neto = Calculos.ejercicio12(horas, valor_hora, porcentaje)
        print("Sueldo bruto:", bruto)
        print("Retención:", retencion)
        print("Sueldo neto:", neto)


if __name__ == "__main__":
    Ejercicio12().ejecutar()
