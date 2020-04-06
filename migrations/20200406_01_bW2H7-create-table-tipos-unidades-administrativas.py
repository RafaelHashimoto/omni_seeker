"""
create table tipos_unidades_administrativas
"""

from yoyo import step

__depends__ = {'20200405_01_NHXKq-create-table-contas-bancarias'}

steps = [
    step(
        "create table tipos_unidades_administrativas ("
            'id SERIAL PRIMARY KEY,'
            'codigo varchar(255),'
            'nome varchar(255)'
        ")",
        "DROP TABLE tipos_unidades_administrativas",
    )
]
