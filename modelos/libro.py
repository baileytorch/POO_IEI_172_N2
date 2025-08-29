from modelos.biblioteca import Biblioteca
from modelos.categoria import Categoria
from modelos.autor import Autor


class Libro(Biblioteca, Categoria, Autor):
    def __init__(self, id_libro, id_biblioteca, id_categoria, id_autor, titulo, paginas, copias, fisico, ubicacion, habilitado):
        super().__init__(id_biblioteca)  # type:ignore
        super().__init__(id_categoria)  # type:ignore
        super().__init__(id_autor)  # type:ignore
        self.id_libro = id_libro
        self.titulo = titulo
        self.paginas = paginas
        self.copias = copias
        self.fisico = fisico
        self.ubicacion = ubicacion
        self.habilitado = habilitado
