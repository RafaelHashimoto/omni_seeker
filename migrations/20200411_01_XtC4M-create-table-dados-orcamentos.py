"""
create table dados_orcamentos
"""

from yoyo import step

__depends__ = {'20200406_07_0BLKD-create-table-ordenadores'}

steps = [
    step(
        "create table dados_orcamentos ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'nu_lei_orcamento varchar(10),'
            'valor_total_fixado_orcamento decimal,'
            'numero_perc_sup_orcamento varchar(100),'
            'valor_total_supl_orcamento decimal,'
            'data_envio_loa timestamp,'
            'data_aprov_loa timestamp,'
            'data_public_loa timestamp'
        ")",
        "DROP TABLE dados_orcamentos"
    )
]


