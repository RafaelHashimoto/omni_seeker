from sqlalchemy import Column, Integer, String
from models.base import Base

class Programa(Base):
    __tablename__ = 'programas'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_programa = Column(String)
    nome_programa = Column(String)


    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_programa = params['codigo_programa']
        self.nome_programa = params['nome_programa']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()