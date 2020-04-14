"""
create table notas_fiscais_liquid
"""

from yoyo import step

__depends__ = {'20200413_01_0JI3z-create-table-estornos-liquidacoes'}

steps = [
    step(
        "create table notas_fiscais_liquid ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_emissao_empenho varchar(255),'
            'numero_empenho varchar(255),'
            'tipo_nota_fiscal varchar(255),'
            'numero_nota_fiscal varchar(255),'
            'data_referencia_nota_fiscal varchar(255),'
            'numero_serie_transito_nota_fiscal varchar(255),'
            'numero_selo_transito_nota_fiscal varchar(255),'
            'numero_serie_nota_fiscal varchar(255),'
            'numero_cgf_emitente_nota_fiscal varchar(255),'
            'uf_emitente_nota_fiscal varchar(255),'
            'data_emissao_nota_fiscal varchar(255),'
            'data_liquidacao_nota_fiscal varchar(255),'
            'nome_resp_liquidacao_nota_fiscal varchar(255),'
            'valor_nota_fiscal varchar(255),'
            'numero_sub_empenho_nota_fiscal varchar(255),'
            'numero_formulario_nota_fiscal varchar(255),'
            'data_limite_nota_fiscal varchar(255)'
        ")",
        "DROP TABLE notas_fiscais_liquid"
    )
]
