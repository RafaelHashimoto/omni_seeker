from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class RecursoEmpenho(Base):
    __tablename__ = 'recursos_empenhos'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    data_emissao_empenho = Column(DateTime)
    numero_empenho = Column(String)
    tipo_recurso_empenho = Column(String)
    numero_sequencial_recurso = Column(String)
    data_celebracao_convenio = Column(String)
    numero_sequencial_convenio = Column(String)
    valor_recurso_empenho = Column(Float)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao_empenho = params['data_emissao_empenho']
        self.numero_empenho = params['numero_empenho']
        self.tipo_recurso_empenho = params['tipo_recurso_empenho']
        self.numero_sequencial_recurso = params['numero_sequencial_recurso']
        self.data_celebracao_convenio = params['data_celebracao_convenio']
        self.numero_sequencial_convenio = params['numero_sequencial_convenio']
        self.valor_recurso_empenho = params['valor_recurso_empenho']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
