"""
create unidades federativas
"""

from yoyo import step

__depends__ = {'20200303_02_qOiH8-create-unidades-federativas'}

steps = [
    step(
        "create table orgaos ("
            "id SERIAL PRIMARY KEY,"
            "codigo_municipio varchar(10),"
            "exercicio_orcamento varchar(10),"
            "codigo_orgao varchar(10),"
            "codigo_tipo_unidade varchar(10),"
            "nome_orgao varchar(255),"
            "cgc_orgao varchar(100)"
        ")",
        "DROP TABLE orgaos",
    )
]
