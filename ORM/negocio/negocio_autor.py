from modelos_orm.autor import Autor
from data.conexion import Session
from sqlalchemy import func
from negocio.negocio_nacionalidad import obtener_nacionalidad


sesion = Session()


def listado_autores():
    listado_autores = sesion.query(Autor).all()

    if len(listado_autores) > 0:
        return listado_autores
    else:
        print('No se han encontrado autores...')


def obtener_autor(buscar_autor: str):
    autor = sesion.query(Autor).filter_by(
        nombre_autor=buscar_autor.title()).first()
    if autor:
        return autor
    else:
        print('No se ha encontrado su comuna...')


def guardar_autor():
    autor = Autor()

    autor.nombre_autor = (  # type: ignore
        input('Ingrese nombre del autor: ')).title()
    autor.pseudonimo = (  # type: ignore
        input('Ingrese pseudónimo del autor: ')).title()
    autor.biografia = input('Ingrese biografía del autor: ')  # type: ignore
    pais = input('Ingrese nombre del país de origen:')
    nacionalidad = obtener_nacionalidad(pais)
    if nacionalidad:
        autor.id_nacionalidad = nacionalidad.id_nacionalidad

    sesion.add(autor)
    try:
        sesion.commit()
        print(f'¡Autor {autor.nombre_autor} guardado con éxito!')
    except Exception as error:
        sesion.rollback()
        print(
            f'No ha sido posible guardar el autor {autor.nombre_autor}, {error}')
    finally:
        sesion.close()
