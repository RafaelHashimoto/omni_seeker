"""
create table balancete_receita_extra_orcamentaria
"""

from yoyo import step

__depends__ = {'20200519_04_jRwbe-create-table-balancete-despesa-extra-orcamentaria'}

steps = [
    step(
        "create table balancete_receita_extra_orcamentaria ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'codigo_conta_extraorcamentaria varchar(100),'
            'data_referencia varchar(10),'
            'tipo_balancete varchar(10),'
            'valor_anulacoes_empenhos_no_mes decimal,'
            'valor_nulacoes_dotacao_ate_mes decimal,'
            'valor_arrecadacao_empenhos_no_mes decimal,'
            'valor_arrecadacao_dotacao_ate_mes decimal'
        ")",
        "DROP TABLE balancete_receita_extra_orcamentaria"
    )
]

