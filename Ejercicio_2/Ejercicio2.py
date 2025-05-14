from datetime import date, time
from typing import List

class Usuario:
    def __init__(self, nombre: str, correo: str):
        self._nombre = nombre
        self._correo = correo
        self._reservas: List[Reserva] = []

    def agregar_reserva(self, reserva: "Reserva") -> None:
        self._reservas.append(reserva)

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def correo(self) -> str:
        return self._correo

    @property
    def reservas(self) -> List["Reserva"]:
        return list(self._reservas)

    def __str__(self) -> str:
        return f"Usuario(nombre={self._nombre}, correo={self._correo})"


class Sala:
    def __init__(self, nombre: str, capacidad: int):
        self._nombre = nombre
        self._capacidad = capacidad
        self._reservas: List[Reserva] = []

    def agregar_reserva(self, reserva: "Reserva") -> None:
        self._reservas.append(reserva)

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def capacidad(self) -> int:
        return self._capacidad

    @property
    def reservas(self) -> List["Reserva"]:
        return list(self._reservas)

    def __str__(self) -> str:
        return f"Sala(nombre={self._nombre}, capacidad={self._capacidad})"


class Reserva:
    def __init__(
        self,
        usuario: Usuario,
        sala: Sala,
        fecha: date,
        hora_inicio: time,
        hora_fin: time
    ):
        self._usuario = usuario
        self._sala = sala
        self._fecha = fecha
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin

        # enlace bidireccional
        usuario.agregar_reserva(self)
        sala.agregar_reserva(self)

    @property
    def usuario(self) -> Usuario:
        return self._usuario

    @property
    def sala(self) -> Sala:
        return self._sala

    @property
    def fecha(self) -> date:
        return self._fecha

    @property
    def hora_inicio(self) -> time:
        return self._hora_inicio

    @property
    def hora_fin(self) -> time:
        return self._hora_fin

    def __str__(self) -> str:
        return (f"Reserva(usuario={self._usuario.nombre}, sala={self._sala.nombre}, "
                f"fecha={self._fecha}, {self._hora_inicio}-{self._hora_fin})")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear entidades
    alice = Usuario("Alice", "alice@example.com")
    sala1 = Sala("Sala Azul", 20)

    # Crear reserva
    r1 = Reserva(alice, sala1, date(2025, 6, 15), time(10, 0), time(12, 0))

    print(alice)
    print(sala1)
    print("Reservas de Alice:", alice.reservas)
    print("Reservas de Sala Azul:", sala1.reservas)
