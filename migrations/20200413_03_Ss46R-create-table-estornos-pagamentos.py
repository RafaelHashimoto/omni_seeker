"""
create table estornos_pagamentos
"""

from yoyo import step

__depends__ = {'20200413_02_Yv3MX-create-table-notas-fiscais-liquid'}

steps = [
    step(
        "create table estornos_pagamentos ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_emissao_empenho timestamp,'
            'numero_empenho varchar(100),'
            'numero_sub_empenho_nota_pagamento varchar(100),'
            'numero_pagamento varchar(100),'
            'data_estorno_pagamento timestamp,'
            'data_referencia_estorno_pagamento varchar(100),'
            'nome_assessor varchar(255),'
            'descricao_justificativa text'
        ")",
        "DROP TABLE estornos_pagamentos"
    )
]
