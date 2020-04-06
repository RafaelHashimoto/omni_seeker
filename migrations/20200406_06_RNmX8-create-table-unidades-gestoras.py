"""
create table unidades_gestoras
"""

from yoyo import step

__depends__ = {'20200406_05_l3U1I-create-table-funcoes'}

steps = [
    step(
        "create table unidades_gestoras ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_unidade_gestora varchar(10),'
            'data_referencia varchar(10),'
            'nome_unidade_gestora varchar(255),'
            'data_criacao timestamp,'
            'data_extincao timestamp,'
            'numero_lei_criacao varchar(10)'
        ")",
        "DROP TABLE unidades_gestoras",
    )
]
