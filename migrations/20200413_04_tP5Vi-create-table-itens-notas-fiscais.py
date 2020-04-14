"""
create table itens_notas_fiscais
"""

from yoyo import step

__depends__ = {'20200413_03_Ss46R-create-table-estornos-pagamentos'}

steps = [
    step(
        "create table itens_notas_fiscais ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_emissao timestamp,'
            'numero_nota_empenho varchar(100),'
            'data_liquidacao varchar(100),'
            'tipo_nota_fiscal varchar(10),'
            'numero_nota_fiscal varchar(100),'
            'numero_item_sequencial varchar(100),'
            'descricao1_item text,'
            'descricao2_item text,'
            'unidade_compra varchar(10),'
            'numero_quantidade_comprada decimal,'
            'valor_unitario_item decimal,'
            'valor_total_item decimal,'
            'codigo_ncm varchar(100)'
        ")",
        "DROP TABLE itens_notas_fiscais"
    )
]