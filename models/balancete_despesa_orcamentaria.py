from models.base import Base
from sqlalchemy import Column, Integer, String, Text, Float

class BalanceteDespesaOrcamentaria(Base):
    __tablename__ = 'balancete_despesa_orcamentaria'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    codigo_funcao = Column(String)
    codigo_subfuncao = Column(String)
    codigo_programa = Column(String)
    codigo_projeto_atividade = Column(String)
    numero_projeto_atividade = Column(String)
    numero_subprojeto_atividade = Column(String)
    codigo_elemento_despesa = Column(String)
    data_referencia = Column(String)
    tipo_balancete = Column(String)
    valor_fixado_orcamento_bal_despesa = Column(Float)
    valor_supl_no_mes = Column(Float)
    valor_supl_ate_mes = Column(Float)
    valor_nulacoes_dotacao_no_mes = Column(Float)
    valor_empenhado_no_mes = Column(Float)
    valor_empenhado_ate_mes = Column(Float)
    valor_saldo_dotacao = Column(Float)
    valor_pago_no_mes = Column(Float)
    valor_pago_ate_mes = Column(Float)
    valor_empenhado_pagar = Column(Float)
    valor_nulacoes_dotacao_ate_mes = Column(Float)
    valor_anulacoes_empenhos_no_mes = Column(Float)
    valor_anulacoes_empenhos_ate_mes = Column(Float)
    valor_liquidado_no_mes = Column(Float)
    valor_liquidado_ate_mes = Column(Float)
    valor_estornos_liquidacao_no_mes = Column(Float)
    valor_estornos_liquidacao_ate_mes = Column(Float)
    valor_estornos_pagos_no_mes = Column(Float)
    valor_estornos_pagos_ate_mes = Column(Float)
    tipo_fonte = Column(String)
    codigo_fonte = Column(String)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.codigo_funcao = params['codigo_funcao']
        self.codigo_subfuncao = params['codigo_subfuncao']
        self.codigo_programa = params['codigo_programa']
        self.codigo_projeto_atividade = params['codigo_projeto_atividade']
        self.numero_projeto_atividade = params['numero_projeto_atividade']
        self.numero_subprojeto_atividade = params['numero_subprojeto_atividade']
        self.codigo_elemento_despesa = params['codigo_elemento_despesa']
        self.data_referencia = params['data_referencia']
        self.tipo_balancete = params['tipo_balancete']
        self.valor_fixado_orcamento_bal_despesa = params['valor_fixado_orcamento_bal_despesa']
        self.valor_supl_no_mes = params['valor_supl_no_mes']
        self.valor_supl_ate_mes = params['valor_supl_ate_mes']
        self.valor_nulacoes_dotacao_no_mes = params['valor_nulacoes_dotacao_no_mes']
        self.valor_empenhado_no_mes = params['valor_empenhado_no_mes']
        self.valor_empenhado_ate_mes = params['valor_empenhado_ate_mes']
        self.valor_saldo_dotacao = params['valor_saldo_dotacao']
        self.valor_pago_no_mes = params['valor_pago_no_mes']
        self.valor_pago_ate_mes = params['valor_pago_ate_mes']
        self.valor_empenhado_pagar = params['valor_empenhado_pagar']
        self.valor_nulacoes_dotacao_ate_mes = params['valor_nulacoes_dotacao_ate_mes']
        self.valor_anulacoes_empenhos_no_mes = params['valor_anulacoes_empenhos_no_mes']
        self.valor_anulacoes_empenhos_ate_mes = params['valor_anulacoes_empenhos_ate_mes']
        self.valor_liquidado_no_mes = params['valor_liquidado_no_mes']
        self.valor_liquidado_ate_mes = params['valor_liquidado_ate_mes']
        self.valor_estornos_liquidacao_no_mes = params['valor_estornos_liquidacao_no_mes']
        self.valor_estornos_liquidacao_ate_mes = params['valor_estornos_liquidacao_ate_mes']
        self.valor_estornos_pagos_no_mes = params['valor_estornos_pagos_no_mes']
        self.valor_estornos_pagos_ate_mes = params['valor_estornos_pagos_ate_mes']
        self.tipo_fonte = params['tipo_fonte']
        self.codigo_fonte = params['codigo_fonte']

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()