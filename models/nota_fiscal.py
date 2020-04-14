from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class NotaFiscalLiquidada(Base):
    __tablename__ = 'notas_fiscais_liquid'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    data_emissao_empenho = Column(DateTime)
    numero_empenho = Column(String)
    data_liquidacao = Column(DateTime)
    tipo_nota_fiscal = Column(String)
    numero_nota_fiscal = Column(String)
    data_referencia = Column(String)
    numero_serie_selo_transito = Column(String)
    numero_selo_transito = Column(String)
    numero_serie = Column(String)
    numero_formulario = Column(String)
    data_limite = Column(DateTime)
    cgf_emitente = Column(String)
    data_emissao = Column(DateTime)
    valor_liquido = Column(Float)
    valor_desconto = Column(Float)
    valor_bruto = Column(Float)
    valor_aliquota_iss = Column(Float)
    valor_base_calculo_iss = Column(Float)
    tipo_emissao = Column(String)
    numero_protocolo_autenticacao = Column(String)


    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao_empenho = params['data_emissao_empenho']
        self.numero_empenho = params['numero_empenho']
        self.data_liquidacao = params['data_liquidacao']
        self.tipo_nota_fiscal = params['tipo_nota_fiscal']
        self.numero_nota_fiscal = params['numero_nota_fiscal']
        self.data_referencia = params['data_referencia']
        self.numero_serie_selo_transito = params['numero_serie_selo_transito']
        self.numero_selo_transito = params['numero_selo_transito']
        self.numero_serie = params['numero_serie']
        self.numero_formulario = params['numero_formulario']
        self.data_limite = params['data_limite']
        self.cgf_emitente = params['cgf_emitente']
        self.data_emissao = params['data_emissao']
        self.valor_liquido = params['valor_liquido']
        self.valor_desconto = params['valor_desconto']
        self.valor_bruto = params['valor_bruto']
        self.valor_aliquota_iss = params['valor_aliquota_iss']
        self.valor_base_calculo_iss = params['valor_base_calculo_iss']
        self.tipo_emissao = params['tipo_emissao']
        self.numero_protocolo_autenticacao = params['numero_protocolo_autenticacao']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
