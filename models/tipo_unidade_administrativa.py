from sqlalchemy import Column, Integer, String
from models.base import Base

class TipoUnidadeAdministrativa(Base):
    __tablename__ = 'tipos_unidades_administrativas'

    id = Column(Integer, primary_key=True)
    codigo = Column(String)

    def __init__(self, params):
        self.codigo = params['codigo_tipo_unidade_administrativa']
        self.nome = params['nome_tipo_unidade_administrativa']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()