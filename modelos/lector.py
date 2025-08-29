from modelos.biblioteca import Biblioteca
from modelos.direccion import Direccion


class Lector(Biblioteca, Direccion):
    def __init__(self, rut_lector, digito_verificador, nombre_lector, correo_lector, id_biblioteca, id_direccion, habilitado):
        super().__init__(id_biblioteca)
        super().__init__(id_direccion)
        self.rut_lector = rut_lector
        self.digito_verificador = digito_verificador
        self.nombre_lector = nombre_lector
        self.correo_lector = correo_lector
        self.habilitado = habilitado
