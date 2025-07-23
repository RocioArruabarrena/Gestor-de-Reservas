from models.usuario import Usuario

class UsuarioRepository:
    def __init__(self):
        self.usuarios = []

    def crear(self, nombre):
        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        return usuario

    def obtener_todos(self):
        return self.usuarios

    def obtener_por_nombre(self, nombre):
        return next((u for u in self.usuarios if u.nombre == nombre), None)

    def actualizar(self, nombre, nuevo_nombre):
        usuario = self.obtener_por_nombre(nombre)
        if usuario:
            usuario.nombre = nuevo_nombre
            return True
        return False

    def eliminar(self, nombre):
        usuario = self.obtener_por_nombre(nombre)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False
