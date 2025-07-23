class Reserva:
    def __init__(self, sala, usuario, fecha, hora):
        self.sala = sala
        self.usuario = usuario
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.sala.nombre} reservado por {self.usuario.nombre}"
