from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base

class GestorUnidadeGestora(Base):
    __tablename__ = 'gestores_unidades_gestoras'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_unidade_gestora = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    cpf_servidor = Column(String)
    codigo_ingresso = Column(String)
    codigo_vinculo = Column(String)
    numero_expediente = Column(String)
    data_inicio_gestao = Column(DateTime)
    data_referencia = Column(String)
    nome_gestor = Column(String)
    data_fim_gestao = Column(String)
    tipo_cargo = Column(String)
    status_ordenador_despesa = Column(Integer)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_unidade_gestora = params['codigo_unidade_gestora']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.cpf_servidor = params['cpf_servidor']
        self.codigo_ingresso = params['codigo_ingresso']
        self.codigo_vinculo = params['codigo_vinculo']
        self.numero_expediente = params['numero_expediente']
        self.data_inicio_gestao = params['data_inicio_gestao'] if params['data_inicio_gestao'] != '' else None
        self.data_referencia = params['data_referencia']
        self.nome_gestor = params['nome_gestor']
        self.data_fim_gestao = params['data_fim_gestao'] if params['data_fim_gestao'] != '' else None
        self.tipo_cargo = params['tipo_cargo']
        self.status_ordenador_despesa = params['status_ordenador_despesa'] if params['status_ordenador_despesa'] != '' else None


    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
