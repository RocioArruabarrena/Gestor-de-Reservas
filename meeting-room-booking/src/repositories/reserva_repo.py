from models.reserva import Reserva

class ReservaRepository:
    def __init__(self):
        self.reservas = []

    def crear(self, sala, usuario, fecha, hora):
        reserva = Reserva(sala, usuario, fecha, hora)
        self.reservas.append(reserva)
        return reserva

    def obtener_todas(self):
        return self.reservas

    def obtener_por_usuario(self, nombre_usuario):
        return [r for r in self.reservas if r.usuario.nombre == nombre_usuario]

    def obtener_por_sala(self, nombre_sala):
        return [r for r in self.reservas if r.sala.nombre == nombre_sala]

    def existe_reserva(self, sala, fecha, hora):
        return any(r.sala.nombre == sala and r.fecha == fecha and r.hora == hora for r in self.reservas)

    def eliminar(self, sala, fecha, hora):
        for r in self.reservas:
            if r.sala.nombre == sala and r.fecha == fecha and r.hora == hora:
                self.reservas.remove(r)
                return True
        return False
