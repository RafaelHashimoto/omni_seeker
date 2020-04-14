from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class NotaPagamento(Base):
    __tablename__ = 'notas_fiscais_liquid'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    data_emissao_empenho = Column(DateTime)
    numero_empenho = Column(String)
    numero_sub_empenho = Column(String)
    numero_nota_pagamento = Column(String)
    data_referencia = Column(String)
    nu_documento_caixa = Column(String)
    data_nota_pagamento = Column(DateTime)
    valor_nota_pagamento = Column(Float)
    valor_empenhado_a_pagar = Column(Float)
    estado_de_estornado = Column(String)
    cpf_pagador = Column(String)
    nome_pagador = Column(String)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao_empenho = params['data_emissao_empenho']
        self.numero_empenho = params['numero_empenho']
        self.numero_sub_empenho = params['numero_sub_empenho']
        self.numero_nota_pagamento = params['numero_nota_pagamento']
        self.data_referencia = params['data_referencia']
        self.nu_documento_caixa = params['nu_documento_caixa']
        self.data_nota_pagamento = params['data_nota_pagamento']
        self.valor_nota_pagamento = params['valor_nota_pagamento']
        self.valor_empenhado_a_pagar = params['valor_empenhado_a_pagar']
        self.estado_de_estornado = params['estado_de_estornado']
        self.cpf_pagador = params['cpf_pagador']
        self.nome_pagador = params['nome_pagador']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
