from sqlalchemy import Column, Float, Integer, String, DateTime
from models.base import Base


class EstornoLiquidacao(Base):
    __tablename__ = 'estornos_liquidacoes'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    data_emissao_empenho = Column(DateTime)
    numero_empenho = Column(String)
    data_liquidacao = Column(DateTime)
    data_estorno_liquidacao = Column(DateTime)
    data_referencia_estorno_liquidacao = Column(String)
    nome_assessor = Column(String)
    descricao_justificativa = Column(String)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao_empenho = params['data_emissao_empenho']
        self.numero_empenho = params['numero_empenho']
        self.data_liquidacao = params['data_liquidacao']
        self.data_estorno_liquidacao = params['data_estorno_liquidacao']
        self.data_referencia_estorno_liquidacao = params['data_referencia_estorno_liquidacao']
        self.nome_assessor = params['nome_assessor']
        self.descricao_justificativa = params['descricao_justificativa']


    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
