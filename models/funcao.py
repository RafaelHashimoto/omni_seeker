from sqlalchemy import Column, Integer, String
from models.base import Base

class Funcao(Base):
    __tablename__ = 'funcoes'

    id = Column(Integer, primary_key=True)
    codigo = Column(String)
    nome = Column(String)

    def __init__(self, params):
        self.codigo = params['codigo_funcao']
        self.nome = params['nome_funcao']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()