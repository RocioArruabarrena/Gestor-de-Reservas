from models.sala import Sala
from models.usuario import Usuario
from services.gestor_reservas import GestorReservas

def main():
    gestor = GestorReservas()

    
    gestor.agregar_sala(Sala("Sala Norte", 10))
    gestor.agregar_sala(Sala("Sala Sur", 5))

   
    usuario1 = Usuario("Daniela")

   
    gestor.hacer_reserva("Sala Norte", usuario1, "2025-05-20", "19:00")
    
    # Intentar reservar la misma sala en el mismo horario
    gestor.hacer_reserva("Sala Norte", usuario1, "2025-05-20", "19:00")

   
    print("\nReservas actuales:")
    gestor.mostrar_reservas()

   
    gestor.cancelar_reserva("Sala Norte", "2025-05-20", "19:00")

 
    print("\nReservas después de cancelar:")
    gestor.mostrar_reservas()

if __name__ == "__main__":
    main()
