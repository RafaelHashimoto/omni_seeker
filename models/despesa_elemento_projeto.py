from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class DespesaElementoProjeto(Base):
    __tablename__ = 'despesa_elemento_projeto'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    codigo_funcao = Column(String)
    codigo_subfuncao = Column(String)
    codigo_programa = Column(String)
    codigo_projeto_atividade = Column(String)
    numero_projeto_atividade = Column(String)
    numero_subprojeto_atividade = Column(String)
    codigo_elemento_despesa = Column(String)
    valor_atual_categoria_economica = Column(Float)
    valor_orcado_categoria_economica = Column(Float)
    tipo_fonte = Column(String)
    codigo_fonte = Column(String)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.codigo_funcao = params['codigo_funcao']
        self.codigo_subfuncao = params['codigo_subfuncao']
        self.codigo_programa = params['codigo_programa']
        self.codigo_projeto_atividade = params['codigo_projeto_atividade']
        self.numero_projeto_atividade = params['numero_projeto_atividade']
        self.numero_subprojeto_atividade = params['numero_subprojeto_atividade']
        self.codigo_elemento_despesa = params['codigo_elemento_despesa']
        self.valor_atual_categoria_economica = params['valor_atual_categoria_economica']
        self.valor_orcado_categoria_economica = params['valor_orcado_categoria_economica']
        self.tipo_fonte = params['tipo_fonte']
        self.codigo_fonte = params['codigo_fonte']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
