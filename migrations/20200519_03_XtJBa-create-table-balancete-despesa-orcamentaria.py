"""
create table balancete_despesa_orcamentaria
"""

from yoyo import step

__depends__ = {'20200519_02_ZAoEQ-create-table-balancete-receita-orcamentaria'}

steps = [
    step(
        "create table balancete_despesa_orcamentaria ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(100),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'codigo_funcao varchar(10),'
            'codigo_subfuncao varchar(100),'
            'codigo_programa varchar(100),'
            'codigo_projeto_atividade varchar(100),'
            'numero_projeto_atividade varchar(100),'
            'numero_subprojeto_atividade varchar(100),'
            'codigo_elemento_despesa varchar(100),'
            'data_referencia varchar(100),'
            'tipo_balancete varchar(100),'
            'valor_fixado_orcamento_bal_despesa decimal,'
            'valor_supl_no_mes decimal,'
            'valor_supl_ate_mes decimal,'
            'valor_nulacoes_dotacao_no_mes decimal,'
            'valor_empenhado_no_mes decimal,'
            'valor_empenhado_ate_mes decimal,'
            'valor_saldo_dotacao decimal,'
            'valor_pago_no_mes decimal,'
            'valor_pago_ate_mes decimal,'
            'valor_empenhado_pagar decimal,'
            'valor_nulacoes_dotacao_ate_mes decimal,'
            'valor_anulacoes_empenhos_no_mes decimal,'
            'valor_anulacoes_empenhos_ate_mes decimal,'
            'valor_liquidado_no_mes decimal,'
            'valor_liquidado_ate_mes decimal,'
            'valor_estornos_liquidacao_no_mes decimal,'
            'valor_estornos_liquidacao_ate_mes decimal,'
            'valor_estornos_pagos_no_mes decimal,'
            'valor_estornos_pagos_ate_mes decimal,'
            'tipo_fonte varchar(10),'
            'codigo_fonte varchar(10)'
        ")",
        "DROP TABLE balancete_despesa_orcamentaria"
    )
]
