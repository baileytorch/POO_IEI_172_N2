from sqlalchemy import Integer, String, Column
from modelos_orm.base import BaseModel


class Nacionalidad(BaseModel):
    id_nacionalidad = Column(Integer, primary_key=True)
    pais = Column(String(length=50))
    nacionalidad = Column(String(length=50))
