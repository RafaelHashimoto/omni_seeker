from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base


class EstornoPagamento(Base):
    __tablename__ = 'estornos_pagamentos'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    data_emissao_empenho = Column(DateTime)
    numero_empenho = Column(String)
    numero_sub_empenho_nota_pagamento = Column(String)
    numero_pagamento = Column(String)
    data_estorno_pagamento = Column(DateTime)
    data_referencia_estorno_pagamento = Column(String)
    nome_assessor = Column(String)
    descricao_justificativa = Column(String)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao_empenho = params['data_emissao_empenho']
        self.numero_empenho = params['numero_empenho']
        self.numero_sub_empenho_nota_pagamento = params['numero_sub_empenho_nota_pagamento']
        self.numero_pagamento = params['numero_pagamento']
        self.data_estorno_pagamento = params['data_estorno_pagamento']
        self.data_referencia_estorno_pagamento = params['data_referencia_estorno_pagamento']
        self.nome_assessor = params['nome_assessor']
        self.descricao_justificativa = params['descricao_justificativa']


    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
