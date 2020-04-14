"""
create table negociantes
"""

from yoyo import step

__depends__ = {'20200413_07_3bmhl-create-table-liquidacoes'}

steps = [
    step(
        "create table negociantes ("
            'id SERIAL PRIMARY KEY,'
            'numero_documento_negociante varchar(100),'
            'codigo_tipo_negociante varchar(10),'
            'nome_negociante varchar(255),'
            'endereco_negociante varchar(255),'
            'fone_negociante varchar(100),'
            'cep_negociante varchar(100),'
            'nome_municipio_negociante varchar(100),'
            'uf_negociante varchar(10)'
        ")",
        "DROP TABLE negociantes"
    )
]


