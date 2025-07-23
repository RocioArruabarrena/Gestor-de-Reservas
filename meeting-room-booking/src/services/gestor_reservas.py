from patterns.singleton import Singleton
from models.reserva import Reserva

class GestorReservas(metaclass=Singleton):
    def __init__(self):
        self.salas = []
        self.reservas = []

    def agregar_sala(self, sala):
        self.salas.append(sala)

    def hacer_reserva(self, sala_nombre, usuario, fecha, hora):
        sala = next((s for s in self.salas if s.nombre == sala_nombre), None)
        if not sala:
            print("Sala no encontrada")
            return

        if any(r.sala.nombre == sala_nombre and r.fecha == fecha and r.hora == hora for r in self.reservas):
            print("La sala ya esta reservada en ese horario")
            return

        reserva = Reserva(sala, usuario, fecha, hora)
        self.reservas.append(reserva)
        print("Reserva realizada con exito")

    def cancelar_reserva(self, sala_nombre, fecha, hora):
        for r in self.reservas:
            if r.sala.nombre == sala_nombre and r.fecha == fecha and r.hora == hora:
                self.reservas.remove(r)
                print("Reserva cancelada")
                return
        print("Reserva no encontrada")

    def mostrar_reservas(self):
        for r in self.reservas:
            print(r)
