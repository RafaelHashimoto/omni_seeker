"""
create table despesa_elemento_projeto
"""

from yoyo import step

__depends__ = {'20200411_05_SfO96-create-table-orcamento-receita'}

steps = [
    step(
        "create table despesa_elemento_projeto ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'codigo_funcao varchar(10),'
            'codigo_subfuncao varchar(10),'
            'codigo_programa varchar(10),'
            'codigo_projeto_atividade varchar(10),'
            'numero_projeto_atividade varchar(10),'
            'numero_subprojeto_atividade varchar(10),'
            'codigo_elemento_despesa varchar(100),'
            'valor_atual_categoria_economica decimal,'
            'valor_orcado_categoria_economica decimal,'
            'tipo_fonte varchar(10),'
            'codigo_fonte varchar(10)'
        ")",
        "DROP TABLE despesa_elemento_projeto"
    )
]