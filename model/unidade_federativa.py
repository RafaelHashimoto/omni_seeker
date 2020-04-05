from sqlalchemy import Column, Integer, String
from model.base import Base

class UnidadeFederativa(Base):
    __tablename__ = 'unidades_federativas'

    id = Column(Integer, primary_key=True)
    codigo = Column(String)
    nome = Column(String)
    sigla = Column(String)

    def __init__(self, params):
        self.codigo = params['codigo_unidade_federacao']
        self.nome = params['nome_unidade_federacao']
        self.sigla = params['sigla_unidade_federacao']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()