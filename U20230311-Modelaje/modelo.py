from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Auto(Base):
    __tablename__= 'tbl_auto'

    idauto = Column(Integer, primary_key=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    año = Column(Integer, nullable=True)

class Cliente(Base):
    __tablename__ = 'tbl_cliente'

    idcliente = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    telefono = Column(String, nullable=True)

class Alquiler(Base):
    __tablename__ = 'tbl_alquiler'

    idalquiler = Column(Integer, primary_key=True)
    idcliente = Column(Integer, ForeignKey('tbl_cliente.idcliente'), nullable=False)
    idauto = Column(Integer, ForeignKey('tbl_auto.idauto'), nullable=False)
    fechalquiler = Column(Date, nullable=False)
    fechadevolucion = Column(Date, nullable=True)
    total = Column(Float, nullable=False)

engine = create_engine('sqlite:///alquiler.db', echo=True) 
Base.metadata.create_all(engine)
