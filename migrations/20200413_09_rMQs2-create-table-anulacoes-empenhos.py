"""
create table anulacoes_empenhos
"""

from yoyo import step

__depends__ = {'20200413_08_m3EXT-create-table-negociantes'}

steps = [
    step(
        "create table anulacoes_empenhos ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_emissao_empenho timestamp,'
            'numero_empenho varchar(10),'
            'numero_anulacao varchar(10),'
            'data_referencia_anulacao varchar(10),'
            'data_anulacao timestamp,'
            'modalidade_anulacao varchar(10),'
            'descricao_anulacao text,'
            'valor_anterior_saldo_dotacao decimal,'
            'valor_anulacao decimal,'
            'valor_atual_saldo_dotacao decimal'
        ")",
        "DROP TABLE negociantes"
    )
]
