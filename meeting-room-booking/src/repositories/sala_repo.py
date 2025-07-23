from models.sala import Sala 

class SalaRepo:
    def __init__(self):
        self.salas = []

    def crear (self, nombre, capacidad):
        sala = Sala (nombre, capacidad)
        self.sala.append(sala)
        return sala
    
    def obtener_por_nombre (self,nombre):
        return next ((s for s in self.salas if s.nombre == nombre), None)
    
    def actualizar (self, nombre, nueva_capacidad):
        sala = self.obtener_por_nombre(nombre)
        if sala:
            sala.capacidad = nueva_capacidad
            return True
        return False
    
    def eliminar (self, nombre):
        sala = self.obtener_por_nombre(nombre)
        if sala: 
            self.salas.remove(sala)
            return True
        return False