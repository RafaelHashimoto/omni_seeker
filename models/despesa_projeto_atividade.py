from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class DespesaProjetoAtividade(Base):
    __tablename__ = 'orcamento_receita'

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
    codigo_tipo_orcamento = Column(String)
    nome_projeto_atividade = Column(String)
    descricao_projeto_atividade = Column(String)
    valor_total_fixado_projeto_atividade = Column(Float)



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
        self.codigo_tipo_orcamento = params['codigo_tipo_orcamento']
        self.nome_projeto_atividade = params['nome_projeto_atividade']
        self.descricao_projeto_atividade = params['descricao_projeto_atividade']
        self.valor_total_fixado_projeto_atividade = params['valor_total_fixado_projeto_atividade']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
