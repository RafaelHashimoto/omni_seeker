"""
create table orcamento_receita
"""

from yoyo import step

__depends__ = {'20200411_04_31H5E-create-table-despesa-projeto-atividade'}

steps = [
    step(
        "create table orcamento_receita ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'codigo_rubrica varchar(100),'
            'descricao_rubrica varchar(255),'
            'valor_previsto decimal,'
            'tipo_fonte varchar(10),'
            'codigo_fonte varchar(10)'
        ")",
        "DROP TABLE orcamento_receita"
    )
]
