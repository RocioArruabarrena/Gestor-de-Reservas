class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Usuario: {self.nombre}"
