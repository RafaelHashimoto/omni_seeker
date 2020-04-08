"""
create table gestores_unidades_gestoras
"""

from yoyo import step

__depends__ = {'20200406_03_8imYv-create-table-contas-extra-orcamentarias'}

steps = [
    step(
        "create table gestores_unidades_gestoras ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_unidade_gestora varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'cpf_servidor varchar(50),'
            'codigo_ingresso varchar(10),'
            'codigo_vinculo varchar(10),'
            'numero_expediente varchar(30),'
            'data_inicio_gestao timestamp,'
            'data_referencia varchar(10),'
            'nome_gestor varchar(255),'
            'data_fim_gestao timestamp,'
            'tipo_cargo varchar(10),'
            'status_ordenador_despesa integer'
        ")",
        "DROP TABLE gestores_unidades_gestoras",
    )
]






