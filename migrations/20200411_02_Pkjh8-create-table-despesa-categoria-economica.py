"""
create table despesa_categoria_economica
"""

from yoyo import step

__depends__ = {'20200411_01_XtC4M-create-table-dados-orcamentos'}

steps = [
    step(
        "create table despesa_categoria_economica ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'codigo_elemento_despesa varchar(100),'
            'nome_elemento_despesa varchar(255),'
            'valor_total_fixado decimal'
        ")",
        "DROP TABLE despesa_categoria_economica"
    )
]
