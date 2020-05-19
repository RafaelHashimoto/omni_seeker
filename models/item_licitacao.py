from sqlalchemy import Column, Float, Integer, String, Text, DateTime
from models.base import Base


class ItemLicitacao(Base):
    __tablename__ = 'itens_licitacoes'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    data_realizacao_licitacao = Column(DateTime)
    numero_licitacao = Column(String)
    numero_sequencial_item_licitacao = Column(String)
    numero_documento_negociante = Column(String)
    descricao_item_licitacao = Column(String)
    valor_vencedor_item_licitacao = Column(Float)
    codigo_tipo_negociante = Column(String)
    descricao_unidade_item_licitacao = Column(String)
    numero_quantidade_item_licitacao = Column(Float)
    valor_unitario_item_licitacao = Column(Float)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.data_realizacao_licitacao = params['data_realizacao_licitacao']
        self.numero_licitacao = params['numero_licitacao']
        self.numero_sequencial_item_licitacao = params['numero_sequencial_item_licitacao']
        self.numero_documento_negociante = params['numero_documento_negociante']
        self.descricao_item_licitacao = params['descricao_item_licitacao']
        self.valor_vencedor_item_licitacao = params['valor_vencedor_item_licitacao']
        self.codigo_tipo_negociante = params['codigo_tipo_negociante']
        self.descricao_unidade_item_licitacao = params['descricao_unidade_item_licitacao']
        self.numero_quantidade_item_licitacao = params['numero_quantidade_item_licitacao']
        self.valor_unitario_item_licitacao = params['valor_unitario_item_licitacao']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
