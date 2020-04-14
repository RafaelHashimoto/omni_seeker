from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class NotaEmpenho(Base):
    __tablename__ = 'negociantes'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    codigo_orgao = Column(String)
    codigo_unidade = Column(String)
    data_emissao_empenho = Column(DateTime)
    numero_empenho = Column(String)
    data_referencia_empenho = Column(String)
    codigo_funcao = Column(String)
    codigo_subfuncao = Column(String)
    codigo_programa = Column(String)
    codigo_projeto_atividade = Column(String)
    numero_projeto_atividade = Column(String)
    numero_subprojeto_atividade = Column(String)
    codigo_elemento_despesa = Column(String)
    modalidade_empenho = Column(String)
    descricao_empenho = Column(String)
    valor_anterior_saldo_dotacao = Column(Float)
    valor_empenhado = Column(Float)
    valor_atual_saldo_dotacao = Column(Float)
    tipo_processo_licitatorio = Column(String)
    numero_documento_negociante = Column(String)
    estado_empenho = Column(String)
    numero_nota_anulacao = Column(String)
    data_emissao_empenho_substituto = Column(DateTime)
    numero_empenho_substituto = Column(String)
    cd_cpf_gestor = Column(String)
    cpf_gestor_contrato = Column(String)
    data_contrato = Column(DateTime)
    numero_contrato = Column(String)
    data_realizacao_licitacao = Column(DateTime)
    numero_licitacao = Column(String)
    codigo_tipo_negociante = Column(String)
    nome_negociante = Column(String)
    endereco_negociante = Column(String)
    fone_negociante = Column(String)
    cep_negociante = Column(String)
    nome_municipio_negociante = Column(String)
    codigo_uf = Column(String)
    tipo_fonte = Column(String)
    codigo_fonte = Column(String)


    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.codigo_orgao = params['codigo_orgao']
        self.codigo_unidade = params['codigo_unidade']
        self.data_emissao_empenho = params['data_emissao_empenho']
        self.numero_empenho = params['numero_empenho']
        self.data_referencia_empenho = params['data_referencia_empenho']
        self.codigo_funcao = params['codigo_funcao']
        self.codigo_subfuncao = params['codigo_subfuncao']
        self.codigo_programa = params['codigo_programa']
        self.codigo_projeto_atividade = params['codigo_projeto_atividade']
        self.numero_projeto_atividade = params['numero_projeto_atividade']
        self.numero_subprojeto_atividade = params['numero_subprojeto_atividade']
        self.codigo_elemento_despesa = params['codigo_elemento_despesa']
        self.modalidade_empenho = params['modalidade_empenho']
        self.descricao_empenho = params['descricao_empenho']
        self.valor_anterior_saldo_dotacao = params['valor_anterior_saldo_dotacao']
        self.valor_empenhado = params['valor_empenhado']
        self.valor_atual_saldo_dotacao = params['valor_atual_saldo_dotacao']
        self.tipo_processo_licitatorio = params['tipo_processo_licitatorio']
        self.numero_documento_negociante = params['numero_documento_negociante']
        self.estado_empenho = params['estado_empenho']
        self.numero_nota_anulacao = params['numero_nota_anulacao']
        self.data_emissao_empenho_substituto = params['data_emissao_empenho_substituto']
        self.numero_empenho_substituto = params['numero_empenho_substituto']
        self.cd_cpf_gestor = params['cd_cpf_gestor']
        self.cpf_gestor_contrato = params['cpf_gestor_contrato']
        self.data_contrato = params['data_contrato']
        self.numero_contrato = params['numero_contrato']
        self.data_realizacao_licitacao = params['data_realizacao_licitacao']
        self.numero_licitacao = params['numero_licitacao']
        self.codigo_tipo_negociante = params['codigo_tipo_negociante']
        self.nome_negociante = params['nome_negociante']
        self.endereco_negociante = params['endereco_negociante']
        self.fone_negociante = params['fone_negociante']
        self.cep_negociante = params['cep_negociante']
        self.nome_municipio_negociante = params['nome_municipio_negociante']
        self.codigo_uf = params['codigo_uf']
        self.tipo_fonte = params['tipo_fonte']
        self.codigo_fonte = params['codigo_fonte']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
