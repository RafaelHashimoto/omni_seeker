"""
create table balancete_receita_orcamentaria
"""

from yoyo import step

__depends__ = {'20200519_01_FTaK2-create-table-itens-licitacoes'}

steps = [
    step(
        "create table balancete_receita_orcamentaria ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'codigo_rubrica varchar(50),'
            'data_referencia varchar(10),'
            'tipo_balancete varchar(10),'
            'valor_previsto_orcamento decimal,'
            'valor_anulacoes_no_mes decimal,'
            'valor_arrecadacao_no_mes decimal,'
            'valor_arrecadacao_ate_mes decimal,'
            'valor_anulacoes_ate_mes decimal,'
            'tipo_fonte varchar(10),'
            'codigo_fonte varchar(10)'
        ")",
        "DROP TABLE balancete_receita_orcamentaria"
    )
]
