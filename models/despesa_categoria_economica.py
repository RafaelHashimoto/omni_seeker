from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class DespesaCategoriaEconomica(Base):
    __tablename__ = 'despesa_categoria_economica'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    codigo_elemento_despesa = Column(String)
    nome_elemento_despesa = Column(String)
    valor_total_fixado = Column(Float)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.codigo_elemento_despesa = params['codigo_elemento_despesa']
        self.nome_elemento_despesa = params['nome_elemento_despesa']
        self.valor_total_fixado = params['valor_total_fixado']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
