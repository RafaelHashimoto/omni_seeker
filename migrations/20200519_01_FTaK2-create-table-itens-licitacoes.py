"""
create table itens_licitacoes
"""

from yoyo import step

__depends__ = {'20200413_13_fTy1u-create-table-cheques-notas-pagamentos'}

steps = [
    step(
        "create table itens_licitacoes ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'data_realizacao_licitacao timestamp,'
            'numero_licitacao varchar(50),'
            'numero_sequencial_item_licitacao integer,'
            'numero_documento_negociante varchar(20),'
            'descricao_item_licitacao varchar(255),'
            'valor_vencedor_item_licitacao decimal,'
            'codigo_tipo_negociante varchar(10),'
            'descricao_unidade_item_licitacao varchar(255),'
            'numero_quantidade_item_licitacao decimal,'
            'valor_unitario_item_licitacao decimal'
        ")",
        "DROP TABLE itens_licitacoes"
    )
]
