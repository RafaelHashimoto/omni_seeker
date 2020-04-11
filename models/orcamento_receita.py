from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class OrcamentoReceita(Base):
    __tablename__ = 'orcamento_receita'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    codigo_rubrica = Column(String)
    descricao_rubrica = Column(String)
    valor_previsto = Column(Float)
    tipo_fonte = Column(String)
    codigo_fonte = Column(String)


    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.codigo_rubrica = params['codigo_rubrica']
        self.descricao_rubrica = params['descricao_rubrica']
        self.valor_previsto = params['valor_previsto']
        self.tipo_fonte = params['tipo_fonte']
        self.codigo_fonte = params['codigo_fonte']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
