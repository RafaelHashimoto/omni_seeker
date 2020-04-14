"""
create table notas_pagamentos
"""

from yoyo import step

__depends__ = {'20200413_04_tP5Vi-create-table-itens-notas-fiscais'}

steps = [
    step(
        "create table notas_pagamentos ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_emissao_empenho decimal,'
            'numero_empenho varchar(100),'
            'numero_sub_empenho varchar(100),'
            'numero_nota_pagamento varchar(100),'
            'data_referencia varchar(100),'
            'nu_documento_caixa varchar(100),'
            'data_nota_pagamento timestamp,'
            'valor_nota_pagamento decimal,'
            'valor_empenhado_a_pagar decimal,'
            'estado_de_estornado varchar(10),'
            'cpf_pagador varchar(255),'
            'nome_pagador varchar(255)'
        ")",
        "DROP TABLE notas_pagamentos"
    )
]
