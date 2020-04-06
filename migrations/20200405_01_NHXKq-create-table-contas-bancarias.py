"""
create table contas_bancarias
"""

from yoyo import step

__depends__ = {'20200303_04_y4n5m-create-tce-request-monitor', '20200330_01_pMPKS-create-table-licitacoes'}

steps = [
    step(
        "create table contas_bancarias ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'numero_banco varchar(50),'
            'numero_agencia varchar(50),'
            'numero_conta varchar(50),'
            'data_abertura varchar(50),'
            'valor_saldo_abertura decimal,'
            'data_referencia varchar(10),'
            'tipo_conta varchar(10),'
            'codigo_funcao varchar(10),'
            'descricao_objetivo text'
        ")",
        "DROP TABLE contas_bancarias",
    )
]
