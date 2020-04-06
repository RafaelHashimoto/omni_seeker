"""
create licitacoes
"""

from yoyo import step

__depends__ = {'20200303_03_ga9Yd-create-orgaos'}

steps = [
    step(
        "create table licitacoes ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'data_realizacao_autuacao_licitacao varchar(100),'
            'numero_licitacao varchar(100),'
            'hora_licitacao varchar(100),'
            'data_emissao_edital varchar(100),'
            'modalidade_licitacao varchar(100),'
            'tipo_licitacao varchar(30),'
            'descricao1_objeto_licitacao text,'
            'descricao2_objeto_licitacao text,'
            'valor_orcado_estimado decimal,'
            'valor_limite_superior decimal ,'
            'cpf_gestor varchar(30),'
            'data_criacao_comissao varchar(100),'
            'numero_comissao varchar(30),'
            'cpf_responsavel_homologacao varchar(30),'
            'nome_responsavel_homologacao varchar(255),'
            'data_realizacao_licitacao varchar(100),'
            'modalidade_processo_administrativo varchar(10),'
            'cpf_responsavel_juridico varchar(30),'
            'nome_responsavel_juridico varchar(255),'
            'data_homologacao varchar(100),'
            'descricao1_justificativa_preco text,'
            'descricao2_justificativa_preco text,'
            'descricao1_motivo_fornecedor text,'
            'descricao2_motivo_fornecedor text,'
            'nome_orgao_ata varchar(255)'
        ")",
        "DROP TABLE licitacoes",
    )
]


