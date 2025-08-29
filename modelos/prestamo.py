from modelos.libro import Libro
from modelos.lector import Lector


class Prestamo():
    def __init__(self, id_prestamo, id_libro, rut_lector, fecha_prestamo, fecha_devolucion, fecha_entrega):
        super().__init__(id_libro)  # type: ignore
        super().__init__(rut_lector)  # type: ignore
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_entrega = fecha_entrega
