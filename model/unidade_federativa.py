from sqlalchemy import Column, Integer, String
from model.base import Base

class Municipio(Base):
    __tablename__ = 'unidades_federativas'

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
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()