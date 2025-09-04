from modelos.comuna import Comuna
from modelos.nacionalidad import Nacionalidad
from data.conexion import Session
from sqlalchemy import func

sesion = Session()

# listado_comunas = sesion.query(Comuna).all()

# if len(listado_comunas) > 0:
#     for comuna in listado_comunas:
#         print(f'{comuna.id_comuna}, {comuna.codigo_comuna}, {comuna.nombre_comuna}')
# else:
#     print('No se han encontrado comunas...')

# comuna = sesion.query(Comuna).filter_by(nombre_comuna='Temuco').first()
# if comuna:
#     print(type(comuna))
#     print(f'{comuna.id_comuna}, {comuna.codigo_comuna}, {comuna.nombre_comuna}')

listado_nacionalidades = sesion.query(Nacionalidad).all()

if len(listado_nacionalidades) > 0:
    for comuna in listado_nacionalidades:
        print(f'{comuna.id_nacionalidad}, {comuna.pais}, {comuna.nacionalidad}')
else:
    print('No se han encontrado paises...')
