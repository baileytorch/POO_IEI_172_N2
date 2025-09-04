from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Comuna(Base):
    __tablename__ = 'comuna'
    id_comuna = Column(Integer, primary_key=True)
    codigo_comuna = Column(String(length=5))
    nombre_comuna = Column(String(length=50))
