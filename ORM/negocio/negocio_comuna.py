from modelos_orm.comuna import Comuna
from data.conexion import Session
from sqlalchemy import func


sesion = Session()


def listado_comunas():
    listado_comunas = sesion.query(Comuna).all()

    if len(listado_comunas) > 0:
        return listado_comunas
    else:
        print('No se han encontrado comunas...')


def obtener_comuna(buscar_comuna: str):
    comuna = sesion.query(Comuna).filter_by(
        nombre_comuna=buscar_comuna.title()).first()
    if comuna:
        return comuna
    else:
        print('No se ha encontrado su comuna...')
