"""
create table programas
"""

from yoyo import step

__depends__ = {'20200411_02_Pkjh8-create-table-despesa-categoria-economica'}

steps = [
    step(
        "create table programas ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_programa varchar(10),'
            'nome_programa varchar(255)'
        ")",
        "DROP TABLE programas"
    )
]