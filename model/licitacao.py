from sqlalchemy import Column, Float, Integer, String, Text
from model.base import Base


class Licitacao(Base):
    __tablename__ = 'licitacoes'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    data_realizacao_autuacao_licitacao = Column(String)
    numero_licitacao = Column(String)
    hora_licitacao = Column(String)
    data_emissao_edital = Column(String)
    modalidade_licitacao = Column(String)
    tipo_licitacao = Column(String)
    descricao1_objeto_licitacao = Column(Text)
    descricao2_objeto_licitacao = Column(Text)
    valor_orcado_estimado = Column(Float)
    valor_limite_superior = Column(Float)
    cpf_gestor = Column(String)
    data_criacao_comissao = Column(String)
    numero_comissao = Column(String)
    cpf_responsavel_homologacao = Column(String)
    nome_responsavel_homologacao = Column(String)
    data_realizacao_licitacao = Column(String)
    modalidade_processo_administrativo = Column(String)
    cpf_responsavel_juridico = Column(String)
    nome_responsavel_juridico = Column(String)
    data_homologacao = Column(String)
    descricao1_justificativa_preco = Column(Text)
    descricao2_justificativa_preco = Column(Text)
    descricao1_motivo_fornecedor = Column(Text)
    descricao2_motivo_fornecedor = Column(Text)
    nome_orgao_ata = Column(Text)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.data_realizacao_autuacao_licitacao = params['data_realizacao_autuacao_licitacao']
        self.numero_licitacao = params['numero_licitacao']
        self.hora_licitacao = params['hora_licitacao']
        self.data_emissao_edital = params['data_emissao_edital']
        self.modalidade_licitacao = params['modalidade_licitacao']
        self.tipo_licitacao = params['tipo_licitacao']
        self.descricao1_objeto_licitacao = params['descricao1_objeto_licitacao']
        self.descricao2_objeto_licitacao = params['descricao2_objeto_licitacao']
        self.valor_orcado_estimado = params['valor_orcado_estimado']
        self.valor_limite_superior = params['valor_limite_superior']
        self.cpf_gestor = params['cpf_gestor']
        self.data_criacao_comissao = params['data_criacao_comissao']
        self.numero_comissao = params['numero_comissao']
        self.cpf_responsavel_homologacao = params['cpf_responsavel_homologacao']
        self.nome_responsavel_homologacao = params['nome_responsavel_homologacao']
        self.data_realizacao_licitacao = params['data_realizacao_licitacao']
        self.modalidade_processo_administrativo = params['modalidade_processo_administrativo']
        self.cpf_responsavel_juridico = params['cpf_responsavel_juridico']
        self.nome_responsavel_juridico = params['nome_responsavel_juridico']
        self.data_homologacao = params['data_homologacao']
        self.descricao1_justificativa_preco = params['descricao1_justificativa_preco']
        self.descricao2_justificativa_preco = params['descricao2_justificativa_preco']
        self.descricao1_motivo_fornecedor = params['descricao1_motivo_fornecedor']
        self.descricao2_motivo_fornecedor = params['descricao2_motivo_fornecedor']
        self.nome_orgao_ata = params['nome_orgao_ata']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()
