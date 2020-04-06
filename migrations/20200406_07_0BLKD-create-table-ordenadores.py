"""
create table ordenadores
"""

from yoyo import step

__depends__ = {'20200406_06_RNmX8-create-table-unidades-gestoras'}

steps = [
    step(
        "create table ordenadores ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_unidade_gestora varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_inclusao_unidade_orcamentaria timestamp,'
            'cpf_servidor varchar(50),'
            'codigo_ingresso varchar(10),'
            'codigo_vinculo varchar(10),'
            'numero_expediente_nomeacao varchar(50),'
            'data_inicio_gestao_ordenador timestamp,'
            'data_referencia_ordenador varchar(10),'
            'nome_ordenador varchar(255),'
            'data_fim_gestao_ordenador timestamp,'
            'tipo_cargo varchar(10)'
        ")",
        "DROP TABLE ordenadores",
    )
]
