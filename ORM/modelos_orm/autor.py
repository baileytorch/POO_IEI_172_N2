from sqlalchemy import Integer, String, ForeignKey, Column
from modelos_orm.base import BaseModel


class Autor(BaseModel):
    id_autor = Column(Integer, primary_key=True)
    nombre_autor = Column(String(100))
    pseudonimo = Column(String(50))
    biografia = Column(String(255))

    id_nacionalidad = Column(Integer, ForeignKey(
        'nacionalidad.id_nacionalidad'))
