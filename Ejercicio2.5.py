from enum import Enum

# Definición de tipos de cuenta
class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta: TipoCuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0   # Valor inicial del saldo es cero

    # Método que imprime los datos de la cuenta
    def imprimir(self):
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta.value}")
        print(f"Saldo = {self.saldo}")

    # Método que consulta el saldo
    def consultar_saldo(self):
        print(f"El saldo actual es = {self.saldo}")

    # Método para consignar
    def consignar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    # Método para retirar
    def retirar(self, valor: float) -> bool:
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        else:
            print("El valor a retirar debe ser mayor que cero y no debe superar el saldo actual.")
            return False


# Programa principal
class Ejercicio25:
  if __name__ == "__main__":
      cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.AHORROS)

      cuenta.imprimir()
      cuenta.consignar(200000)
      cuenta.consignar(300000)
      cuenta.retirar(400000)
