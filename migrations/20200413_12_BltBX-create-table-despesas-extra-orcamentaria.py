"""
create table despesas_extra_orcamentaria
"""

from yoyo import step

__depends__ = {'20200413_11_5rpgy-create-table-notas-empenhos'}

steps = [
    step(
        "create table despesas_extra_orcamentaria ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'codigo_conta_extraorcamentaria varchar(100),'
            'numero_banco varchar(100),'
            'numero_agencia varchar(100),'
            'numero_conta varchar(100),'
            'numero_documento_despesa_extra varchar(100),'
            'data_referencia_documentacao varchar(100),'
            'numero_documento_caixa varchar(100),'
            'data_emissao_despesa_extra timestamp,'
            'valor_documento_despesa_extra decimal,'
            'valor_deducao_despesa_extra decimal,'
            'tipo_documento_despesa_extra varchar(100),'
            'status_estorno_despesa_extra varchar(100),'
            'nome_credor_despesa_extra varchar(255)'
        ")",
        "DROP TABLE despesas_extra_orcamentaria"
    )
]
