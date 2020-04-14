"""
create table notas_fiscais
"""

from yoyo import step

__depends__ = {'20200413_05_MVpXB-create-table-notas-pagamentos'}

steps = [
    step(
        "create table notas_fiscais ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_emissao_empenho timestamp,'
            'numero_empenho varchar(20),'
            'data_liquidacao timestamp,'
            'tipo_nota_fiscal varchar(10),'
            'numero_nota_fiscal varchar(200),'
            'data_referencia varchar(30),'
            'numero_serie_selo_transito varchar(100),'
            'numero_selo_transito varchar(100),'
            'numero_serie varchar(100),'
            'numero_formulario varchar(100),'
            'data_limite timestamp,'
            'cgf_emitente varchar(100),'
            'data_emissao timestamp,'
            'valor_liquido decimal,'
            'valor_desconto decimal,'
            'valor_bruto decimal,'
            'valor_aliquota_iss decimal,'
            'valor_base_calculo_iss decimal,'
            'tipo_emissao varchar(100),'
            'numero_protocolo_autenticacao varchar(100)'
        ")",
        "DROP TABLE notas_fiscais"
    )
]
