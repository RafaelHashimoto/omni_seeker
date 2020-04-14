"""
create table recursos_empenhos
"""

from yoyo import step

__depends__ = {'20200413_09_rMQs2-create-table-anulacoes-empenhos'}

steps = [
    step(
        "create table recursos_empenhos ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_emissao_empenho timestamp,'
            'numero_empenho varchar(100),'
            'tipo_recurso_empenho varchar(10),'
            'numero_sequencial_recurso varchar(10),'
            'data_celebracao_convenio varchar(255),'
            'numero_sequencial_convenio varchar(255),'
            'valor_recurso_empenho decimal'
        ")",
        "DROP TABLE recursos_empenhos"
    )
]
