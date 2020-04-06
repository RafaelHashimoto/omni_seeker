"""
create table unidades_orcamentarias
"""

from yoyo import step

__depends__ = {'20200406_01_bW2H7-create-table-tipos-unidades-administrativas'}

steps = [
    step(
         "create table unidades_orcamentarias ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'codigo_tipo_unidade varchar(10),'
            'nome_unidade varchar(255),'
            'tipo_administracao_unidade varchar(10)'
        ")",
        "DROP TABLE unidades_orcamentarias",
    )
]
