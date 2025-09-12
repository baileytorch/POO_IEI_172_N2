from sqlalchemy import Integer, String, Column
from modelos_orm.base import BaseModel


class Comuna(BaseModel):
    id_comuna = Column(Integer, primary_key=True)
    codigo_comuna = Column(String(length=5))
    nombre_comuna = Column(String(length=50))
