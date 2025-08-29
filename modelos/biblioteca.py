from modelos.direccion import Direccion


class Biblioteca(Direccion):
    def __init__(self, id_biblioteca=0, nombre_biblioteca='', id_direccion=0, web='', habilitado=1):
        super().__init__(id_direccion)  # type:ignore
        self.id_biblioteca = id_biblioteca
        self.nombre_biblioteca = nombre_biblioteca
        self.web = web
        self.habilitado = habilitado
