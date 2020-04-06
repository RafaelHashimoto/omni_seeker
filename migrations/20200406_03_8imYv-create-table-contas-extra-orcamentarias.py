"""
create table contas_extra_orcamentarias
"""

from yoyo import step

__depends__ = {'20200406_02_uMDSQ-create-table-unidades-orcamentarias'}

steps = [
    step(
         "create table contas_extra_orcamentarias ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_conta_extra_orc varchar(100),'
            'data_referencia_doc varchar(10),'
            'desc_conta_extra_orc varchar(255),'
            'vl_saldo_ini decimal'
        ")",
        "DROP TABLE contas_extra_orcamentarias",
    )
]



