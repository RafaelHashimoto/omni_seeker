from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class ChequeNotaPagamento(Base):
    __tablename__ = 'cheques_notas_pagamentos'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_unidade = Column(String)
    data_emissao_empenho = Column(DateTime)
    numero_empenho = Column(String)
    numero_pagamento = Column(String)
    numero_banco = Column(String)
    numero_agencia = Column(String)
    numero_conta = Column(String)
    numero_cheque = Column(String)
    data_referencia_cheque = Column(String)
    data_emissao_cheque = Column(DateTime)
    valor_cheque = Column(Float)
    tipo_documento_bancario = Column(String)
    codigo_orgao = Column(String)
    numero_doc_ng = Column(String)
    nome_negociante_ng = Column(String)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao_empenho = params['data_emissao_empenho']
        self.numero_empenho = params['numero_empenho']
        self.numero_pagamento = params['numero_pagamento']
        self.numero_banco = params['numero_banco']
        self.numero_agencia = params['numero_agencia']
        self.numero_conta = params['numero_conta']
        self.numero_cheque = params['numero_cheque']
        self.data_referencia_cheque = params['data_referencia_cheque']
        self.data_emissao_cheque = params['data_emissao_cheque']
        self.valor_cheque = params['valor_cheque']
        self.tipo_documento_bancario = params['tipo_documento_bancario']
        self.codigo_orgao = params['codigo_orgao']
        self.numero_doc_ng = params['numero_doc_ng']
        self.nome_negociante_ng = params['nome_negociante_ng']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
