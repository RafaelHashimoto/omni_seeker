from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base

class UnidadeGestora(Base):
    __tablename__ = 'unidades_gestoras'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_unidade_gestora = Column(String)
    data_referencia = Column(String)
    nome_unidade_gestora = Column(String)
    data_criacao = Column(DateTime)
    data_extincao = Column(DateTime)
    numero_lei_criacao = Column(String)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_unidade_gestora = params['codigo_unidade_gestora']
        self.data_referencia = params['data_referencia']
        self.nome_unidade_gestora = params['nome_unidade_gestora']
        self.data_criacao = params['data_criacao'] if params['data_criacao'] != '' else None
        self.data_extincao = params['data_extincao'] if params['data_extincao'] != '' else None
        self.numero_lei_criacao = params['numero_lei_criacao']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
