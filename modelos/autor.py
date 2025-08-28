from modelos.nacionalidad import Nacionalidad


class Autor(Nacionalidad):
    def __init__(self, id_autor, nombre_autor, pseudonimo, id_nacionalidad, bio):
        super().__init__(id_nacionalidad)  # type: ignore
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.pseudonimo = pseudonimo
        self.bio = bio
