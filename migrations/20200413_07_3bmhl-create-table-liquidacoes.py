"""
create table liquidacoes
"""

from yoyo import step

__depends__ = {'20200413_06_KNECY-create-table-notas-fiscais'}

steps = [
    step(
        "create table liquidacoes ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_emissao_empenho timestamp,'
            'numero_empenho varchar(100),'
            'data_liquidacao timestamp,'
            'data_referencia_liquidacao varchar(10),'
            'nome_responsavel_liquidacao varchar(200),'
            'numero_sub_empenho_liquidacao varchar(10),'
            'valor_liquidado decimal,'
            'estado_de_estorno varchar(10),'
            'estado_folha varchar(10),'
            'cpf_responsavel_liquidacao varchar(100)'
        ")",
        "DROP TABLE liquidacoes"
    )
]
