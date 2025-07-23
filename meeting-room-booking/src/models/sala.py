class Sala:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad

    def __str__(self):
        return f"Sala: {self.nombre} - Capacidad: {self.capacidad}"
