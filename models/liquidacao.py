from sqlalchemy import Column, Float, Integer, String, Text, DateTime
from models.base import Base


class Liquidacao(Base):
    __tablename__ = 'liquidacoes'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    data_emissao_empenho = Column(DateTime)
    numero_empenho = Column(String)
    data_liquidacao = Column(DateTime)
    data_referencia_liquidacao = Column(String)
    nome_responsavel_liquidacao = Column(String)
    numero_sub_empenho_liquidacao = Column(String)
    valor_liquidado = Column(Float)
    estado_de_estorno = Column(String)
    estado_folha = Column(String)
    cpf_responsavel_liquidacao = Column(String)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao_empenho = params['data_emissao_empenho']
        self.numero_empenho = params['numero_empenho']
        self.data_liquidacao = params['data_liquidacao']
        self.data_referencia_liquidacao = params['data_referencia_liquidacao']
        self.nome_responsavel_liquidacao = params['nome_responsavel_liquidacao']
        self.numero_sub_empenho_liquidacao = params['numero_sub_empenho_liquidacao']
        self.valor_liquidado = params['valor_liquidado']
        self.estado_de_estorno = params['estado_de_estorno']
        self.estado_folha = params['estado_folha']
        self.cpf_responsavel_liquidacao = params['cpf_responsavel_liquidacao']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
