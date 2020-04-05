from sqlalchemy import Column, Integer, String
from models.base import Base

class Municipio(Base):
    __tablename__ = 'municipios'

    id = Column(Integer, primary_key=True)
    codigo = Column(String)
    nome = Column(String)
    codigo_unidade_federacao = Column(Integer)
    geoibge_id = Column(String)

    def __init__(self, params):
        self.codigo = params['codigo_municipio']
        self.nome = params['nome_municipio']
        self.geoibge_id = params['geoibgeId']
        self.codigo_unidade_federacao = params['geoibgeId'][:2]

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()

    @classmethod
    def by_id_range(cls, id):
        return cls.session.query(cls).filter(cls.id >= id)

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()