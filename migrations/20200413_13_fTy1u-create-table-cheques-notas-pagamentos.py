"""
create table cheques_notas_pagamentos
"""

from yoyo import step

__depends__ = {'20200413_12_BltBX-create-table-despesas-extra-orcamentaria'}

steps = [
    step(
        "create table cheques_notas_pagamentos ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio  varchar(10),'
            'exercicio_orcamento  varchar(10),'
            'codigo_unidade  varchar(10),'
            'data_emissao_empenho timestamp,'
            'numero_empenho  varchar(100),'
            'numero_pagamento  varchar(100),'
            'numero_banco  varchar(100),'
            'numero_agencia  varchar(100),'
            'numero_conta  varchar(100),'
            'numero_cheque  varchar(100),'
            'data_referencia_cheque  varchar(20),'
            'data_emissao_cheque timestamp,'
            'valor_cheque decimal,'
            'tipo_documento_bancario  varchar(20),'
            'codigo_orgao  varchar(20),'
            'numero_doc_ng  varchar(20),'
            'nome_negociante_ng  varchar(255)'
        ")",
        "DROP TABLE cheques_notas_pagamentos"
    )
]
