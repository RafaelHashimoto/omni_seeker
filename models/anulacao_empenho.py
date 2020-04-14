from sqlalchemy import Column, Float, Integer, String, DateTime
from models.base import Base


class AnulacaoEmpenho(Base):
    __tablename__ = 'anulacoes_empenhos'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    data_emissao_empenho = Column(DateTime)
    numero_empenho = Column(String)
    numero_anulacao = Column(String)
    data_referencia_anulacao = Column(String)
    data_anulacao = Column(DateTime)
    modalidade_anulacao = Column(String)
    descricao_anulacao = Column(String)
    valor_anterior_saldo_dotacao = Column(Float)
    valor_anulacao = Column(Float)
    valor_atual_saldo_dotacao = Column(Float)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao_empenho = params['data_emissao_empenho']
        self.numero_empenho = params['numero_empenho']
        self.numero_anulacao = params['numero_anulacao']
        self.data_referencia_anulacao = params['data_referencia_anulacao']
        self.data_anulacao = params['data_anulacao']
        self.modalidade_anulacao = params['modalidade_anulacao']
        self.descricao_anulacao = params['descricao_anulacao']
        self.valor_anterior_saldo_dotacao = params['valor_anterior_saldo_dotacao']
        self.valor_anulacao = params['valor_anulacao']
        self.valor_atual_saldo_dotacao = params['valor_atual_saldo_dotacao']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
