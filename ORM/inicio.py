from negocio.negocio_comuna import listado_comunas, obtener_comuna
from negocio.negocio_nacionalidad import listado_nacionalidades, obtener_nacionalidad
from negocio.negocio_autor import listado_autores, obtener_autor, guardar_autor
from prettytable import PrettyTable

tabla_comunas = PrettyTable()
tabla_comunas.field_names = ['Id', 'Código Comuna', 'Nombre Comuna']
tabla_nacionalidades = PrettyTable()
tabla_nacionalidades.field_names = ['Id', 'País', 'Nacionalidad']
tabla_autores = PrettyTable()
tabla_autores.field_names = ['Id', 'Nombre', 'Pseudónimo', 'Biografía']


def menu_principal():
    print('\nGestión de Biblioteca')
    print('=====================\n')
    print('[1] Listado Comunas')
    print('[2] Listado Nacionalidades')
    print('[3] Buscar Comuna')
    print('[4] Buscar Nacionalidad')
    print('[5] Listado Autores')
    print('[6] Agregar Autor')
    print('[0] Salir')


def principal():
    while True:
        menu_principal()
        opcion = input('Seleccione su opción: ')
        if opcion == '1':
            comunas = []
            comunas = listado_comunas()
            if comunas:
                for comuna in comunas:
                    tabla_comunas.add_row(
                        [comuna.id_comuna, comuna.codigo_comuna, comuna.nombre_comuna])
            print()
            print(tabla_comunas)

        elif opcion == '2':
            nacionalidades = []
            nacionalidades = listado_nacionalidades()
            if nacionalidades:
                for autor in nacionalidades:
                    tabla_nacionalidades.add_row(
                        [autor.id_nacionalidad, autor.pais, autor.nacionalidad])
            print()
            print(tabla_nacionalidades)

        elif opcion == '3':
            comuna_buscar = input('Ingrese el nombre de la comuna a buscar: ')
            comuna_encontrada = obtener_comuna(comuna_buscar)
            if comuna_encontrada:
                print(
                    f'\nID: {comuna_encontrada.id_comuna} Código: {comuna_encontrada.codigo_comuna} Nombre:{comuna_encontrada.nombre_comuna}')

        elif opcion == '4':
            pais_buscar = input('Ingrese el nombre del país a buscar: ')
            nacionalidad_encontrada = obtener_nacionalidad(pais_buscar)
            if nacionalidad_encontrada:
                print(
                    f'\nID: {nacionalidad_encontrada.id_nacionalidad} País: {nacionalidad_encontrada.pais} Nacionalidad: {nacionalidad_encontrada.nacionalidad}')

        elif opcion == '5':
            autores = []
            autores = listado_autores()
            if autores:
                for autor in autores:
                    tabla_autores.add_row(
                        [autor.id_autor, autor.nombre_autor, autor.pseudonimo, autor.biografia])
            print()
            print(tabla_autores)

        elif opcion == '6':
            guardar_autor()

        elif opcion == '0':
            print('Saliendo...')
            break
        else:
            print('Opción NO corresponde... Seleccione nuevamente')


principal()
