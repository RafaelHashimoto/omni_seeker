from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class DespesaExtraOrcamentaria(Base):
    __tablename__ = 'despesas_extra_orcamentaria'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    codigo_conta_extraorcamentaria = Column(String)
    numero_banco = Column(String)
    numero_agencia = Column(String)
    numero_conta = Column(String)
    numero_documento_despesa_extra = Column(String)
    data_referencia_documentacao = Column(DateTime)
    numero_documento_caixa = Column(String)
    data_emissao_despesa_extra = Column(String)
    valor_documento_despesa_extra = Column(Float)
    valor_deducao_despesa_extra = Column(Float)
    tipo_documento_despesa_extra = Column(String)
    status_estorno_despesa_extra = Column(String)
    nome_credor_despesa_extra = Column(String)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.codigo_conta_extraorcamentaria = params['codigo_conta_extraorcamentaria']
        self.numero_banco = params['numero_banco']
        self.numero_agencia = params['numero_agencia']
        self.numero_conta = params['numero_conta']
        self.numero_documento_despesa_extra = params['numero_documento_despesa_extra']
        self.data_referencia_documentacao = params['data_referencia_documentacao']
        self.numero_documento_caixa = params['numero_documento_caixa']
        self.data_emissao_despesa_extra = params['data_emissao_despesa_extra']
        self.valor_documento_despesa_extra = params['valor_documento_despesa_extra']
        self.valor_deducao_despesa_extra = params['valor_deducao_despesa_extra']
        self.tipo_documento_despesa_extra = params['tipo_documento_despesa_extra']
        self.status_estorno_despesa_extra = params['status_estorno_despesa_extra']
        self.nome_credor_despesa_extra = params['nome_credor_despesa_extra']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
