"""
create table funcoes
"""

from yoyo import step

__depends__ = {'20200406_04_2C1Pb-create-table-gestores-unidades-gestoras'}

steps = [
    step(
        "create table funcoes ("
            'id SERIAL PRIMARY KEY,'
            'codigo varchar(255),'
            'nome varchar(255)'
        ")",
        "DROP TABLE funcoes",
    )
]
