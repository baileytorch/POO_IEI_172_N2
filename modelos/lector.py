from modelos.biblioteca import Biblioteca
from modelos.direccion import Direccion


class Lector(Biblioteca, Direccion):
    def __init__(self, id_lector, rut, digito_verificador, nombre_lector, id_biblioteca, id_direccion, habilitado):
        super().__init__(id_biblioteca)
        super().__init__(id_direccion)
        self.id_lector = id_lector
        self.rut = rut
        self.digito_verificador = digito_verificador
        self.nombre_lector = nombre_lector
        self.habilitado = habilitado
