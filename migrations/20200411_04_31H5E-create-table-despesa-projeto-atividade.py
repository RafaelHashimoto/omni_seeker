"""
create table despesa_projeto_atividade
"""

from yoyo import step

__depends__ = {'20200411_03_VsfFL-create-table-programas'}

steps = [
    step(
        "create table despesa_projeto_atividade ("
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
            'codigo_tipo_orcamento varchar(10),'
            'nome_projeto_atividade text,'
            'descricao_projeto_atividade text,'
            'valor_total_fixado_projeto_atividade decimal'
        ")",
        "DROP TABLE despesa_projeto_atividade"
    )
]
