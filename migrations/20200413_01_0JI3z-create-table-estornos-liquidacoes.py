"""
create table estornos_liquidacoes
"""

from yoyo import step

__depends__ = {'20200411_06_lYbLu-create-table-despesa-elemento-projeto'}

steps = [
    step(
        "create table estornos_liquidacoes ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(30),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_emissao_empenho timestamp,'
            'numero_empenho varchar(100),'
            'data_liquidacao timestamp,'
            'data_estorno_liquidacao timestamp,'
            'data_referencia_estorno_liquidacao varchar(100),'
            'nome_assessor varchar(255),'
            'descricao_justificativa text'
        ")",
        "DROP TABLE estornos_liquidacoes"
    )
]
