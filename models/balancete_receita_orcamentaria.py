from models.base import Base
from sqlalchemy import Column, Integer, String, Text, Float

class BalanceteReceitaOrcamentaria(Base):
    __tablename__ = 'balancete_receita_orcamentaria'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    codigo_rubrica = Column(String)
    data_referencia = Column(String)
    tipo_balancete = Column(String)
    valor_previsto_orcamento = Column(Float)
    valor_anulacoes_no_mes = Column(Float)
    valor_arrecadacao_no_mes = Column(Float)
    valor_arrecadacao_ate_mes = Column(Float)
    valor_anulacoes_ate_mes = Column(Float)
    tipo_fonte = Column(String)
    codigo_fonte = Column(String)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.codigo_rubrica = params['codigo_rubrica']
        self.data_referencia = params['data_referencia']
        self.tipo_balancete = params['tipo_balancete '] #realmente tem um espaço depois do texto
        self.valor_previsto_orcamento = params['valor_previsto_orcamento']
        self.valor_anulacoes_no_mes = params['valor_anulacoes_no_mes']
        self.valor_arrecadacao_no_mes = params['valor_arrecadacao_no_mes']
        self.valor_arrecadacao_ate_mes = params['valor_arrecadacao_ate_mes']
        self.valor_anulacoes_ate_mes = params['valor_anulacoes_ate_mes']
        self.tipo_fonte = params['tipo_fonte']
        self.codigo_fonte = params['codigo_fonte']

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()