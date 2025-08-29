from modelos.biblioteca import Biblioteca as biblio

biblioteca = biblio()

biblioteca.id_biblioteca = 1
biblioteca.nombre_biblioteca = 'Pablo Neruda'
biblioteca.id_direccion = 1
print(biblioteca.nombre_biblioteca)
