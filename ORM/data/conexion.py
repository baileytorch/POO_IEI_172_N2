from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

cadena_conexion = 'mysql+mysqlconnector://root:@localhost:3306/iei_172_n2'
motordb = create_engine(cadena_conexion)
Session = sessionmaker(bind=motordb)
