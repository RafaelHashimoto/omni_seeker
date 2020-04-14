from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class NotaFiscalLiquidada(Base):
    __tablename__ = 'notas_fiscais_liquid'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    data_emissao_empenho = Column(String)
    numero_empenho = Column(String)
    tipo_nota_fiscal = Column(String)
    numero_nota_fiscal = Column(String)
    data_referencia_nota_fiscal = Column(String)
    numero_serie_transito_nota_fiscal = Column(String)
    numero_selo_transito_nota_fiscal = Column(String)
    numero_serie_nota_fiscal = Column(String)
    numero_cgf_emitente_nota_fiscal = Column(String)
    uf_emitente_nota_fiscal = Column(String)
    data_emissao_nota_fiscal = Column(String)
    data_liquidacao_nota_fiscal = Column(String)
    nome_resp_liquidacao_nota_fiscal = Column(String)
    valor_nota_fiscal = Column(String)
    numero_sub_empenho_nota_fiscal = Column(String)
    numero_formulario_nota_fiscal = Column(String)
    data_limite_nota_fiscal = Column(String)


    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao_empenho = params['data_emissao_empenho']
        self.numero_empenho = params['numero_empenho']
        self.tipo_nota_fiscal = params['tipo_nota_fiscal']
        self.numero_nota_fiscal = params['numero_nota_fiscal']
        self.data_referencia_nota_fiscal = params['data_referencia_nota_fiscal']
        self.numero_serie_transito_nota_fiscal = params['numero_serie_transito_nota_fiscal']
        self.numero_selo_transito_nota_fiscal = params['numero_selo_transito_nota_fiscal']
        self.numero_serie_nota_fiscal = params['numero_serie_nota_fiscal']
        self.numero_cgf_emitente_nota_fiscal = params['numero_cgf_emitente_nota_fiscal']
        self.uf_emitente_nota_fiscal = params['uf_emitente_nota_fiscal']
        self.data_emissao_nota_fiscal = params['data_emissao_nota_fiscal']
        self.data_liquidacao_nota_fiscal = params['data_liquidacao_nota_fiscal']
        self.nome_resp_liquidacao_nota_fiscal = params['nome_resp_liquidacao_nota_fiscal']
        self.valor_nota_fiscal = params['valor_nota_fiscal']
        self.numero_sub_empenho_nota_fiscal = params['numero_sub_empenho_nota_fiscal']
        self.numero_formulario_nota_fiscal = params['numero_formulario_nota_fiscal']
        self.data_limite_nota_fiscal = params['data_limite_nota_fiscal']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
