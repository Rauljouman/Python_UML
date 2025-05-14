class Vehiculo:
    def __init__(self, marca: str):
        self.marca = marca

class Motor:
    def __init__(self, tipo: str):
        self.tipo = tipo

class Coche(Vehiculo):
    def __init__(self, marca: str, modelo: str, motor: Motor):
        super().__init__(marca)
        self.modelo = modelo
        self.motor = motor

class Camion(Vehiculo):
    def __init__(self, marca: str, capacidad_carga: float, motor: Motor):
        super().__init__(marca)
        self.capacidad_carga = capacidad_carga
        self.motor = motor

if __name__ == "__main__":
    m = Motor("Diésel")
    coche = Coche("Toyota", "Corolla", m)
    camion = Camion("Volvo", 12_000.0, m)

    print(f"Coche: {coche.marca} {coche.modelo}, motor {coche.motor.tipo}")
    print(f"Camión: {camion.marca}, carga {camion.capacidad_carga} kg, motor {camion.motor.tipo}")
