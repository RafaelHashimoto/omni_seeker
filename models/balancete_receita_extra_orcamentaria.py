from models.base import Base
from sqlalchemy import Column, Integer, String, Text, Float

class BalanceteReceitaExtraOrcamentaria(Base):
    __tablename__ = 'balancete_receita_extra_orcamentaria'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    codigo_conta_extraorcamentaria = Column(String)
    data_referencia = Column(String)
    tipo_balancete = Column(String)
    valor_anulacoes_empenhos_no_mes = Column(Float)
    valor_nulacoes_dotacao_ate_mes = Column(Float)
    valor_arrecadacao_empenhos_no_mes = Column(Float)
    valor_arrecadacao_dotacao_ate_mes = Column(Float)



    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.codigo_conta_extraorcamentaria = params['codigo_conta_extraorcamentaria']
        self.data_referencia = params['data_referencia']
        self.tipo_balancete = params['tipo_balancete '] #realmente tem um espaço depois do texto
        self.valor_anulacoes_empenhos_no_mes = params['valor_anulacoes_empenhos_no_mes']
        self.valor_nulacoes_dotacao_ate_mes = params['valor_nulacoes_dotacao_ate_mes']
        self.valor_arrecadacao_empenhos_no_mes = params['valor_arrecadacao_empenhos_no_mes']
        self.valor_arrecadacao_dotacao_ate_mes = params['valor_arrecadacao_dotacao_ate_mes']

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

