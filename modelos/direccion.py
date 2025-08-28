from modelos.comuna import Comuna


class Direccion(Comuna):
    def __init__(self, id_direccion=0, codigo_comuna='', calle='', numero=''):
        super().__init__(codigo_comuna)  # type: ignore
        self.id_direccion = id_direccion
        self.calle = calle
        self.numero = numero
