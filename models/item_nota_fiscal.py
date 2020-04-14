from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class ItemNotaFiscal(Base):
    __tablename__ = 'itens_notas_fiscais'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    data_emissao = Column(DateTime)
    numero_nota_empenho = Column(String)
    data_liquidacao = Column(DateTime)
    tipo_nota_fiscal = Column(String)
    numero_nota_fiscal = Column(String)
    numero_item_sequencial = Column(String)
    descricao1_item = Column(String)
    descricao2_item = Column(String)
    unidade_compra = Column(String)
    numero_quantidade_comprada = Column(Float)
    valor_unitario_item = Column(Float)
    valor_total_item = Column(Float)
    codigo_ncm = Column(String)


    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao = params['data_emissao']
        self.numero_nota_empenho = params['numero_nota_empenho']
        self.data_liquidacao = params['data_liquidacao']
        self.tipo_nota_fiscal = params['tipo_nota_fiscal']
        self.numero_nota_fiscal = params['numero_nota_fiscal']
        self.numero_item_sequencial = params['numero_item_sequencial']
        self.descricao1_item = params['descricao1_item']
        self.descricao2_item = params['descricao2_item']
        self.unidade_compra = params['unidade_compra']
        self.numero_quantidade_comprada = params['numero_quantidade_comprada']
        self.valor_unitario_item = params['valor_unitario_item']
        self.valor_total_item = params['valor_total_item']
        self.codigo_ncm = params['codigo_ncm']


    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
