from modelos_orm.nacionalidad import Nacionalidad
from data.conexion import Session
from sqlalchemy import func

sesion = Session()


def listado_nacionalidades():
    listado_nacionalidades = sesion.query(Nacionalidad).all()

    if len(listado_nacionalidades) > 0:
        return listado_nacionalidades
    else:
        print('No se han encontrado paises...')


def obtener_nacionalidad(buscar_pais: str):
    nacionalidad = sesion.query(
        Nacionalidad).filter_by(pais=buscar_pais.title()).first()

    if nacionalidad:
        return nacionalidad
    else:
        print('No se ha encontrado su país...')
