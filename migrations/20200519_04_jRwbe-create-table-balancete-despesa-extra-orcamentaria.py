"""
create table balancete_despesa_extra_orcamentaria
"""

from yoyo import step

__depends__ = {'20200519_03_XtJBa-create-table-balancete-despesa-orcamentaria'}

steps = [
    step(
        "create table balancete_despesa_extra_orcamentaria ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'codigo_conta_extraorcamentaria varchar(100),'
            'data_referencia varchar(10),'
            'tipo_balancete varchar(10),'
            'valor_anulacao_no_mes decimal,'
            'valor_anulacao_ate_mes decimal,'
            'valor_pago_no_mes decimal,'
            'valor_pago_ate_mes decimal'
        ")",
        "DROP TABLE balancete_despesa_extra_orcamentaria"
    )
]
