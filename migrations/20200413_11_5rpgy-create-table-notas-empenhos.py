"""
create table notas_empenhos
"""

from yoyo import step

__depends__ = {'20200413_10_0keBH-create-table-recursos-empenhos'}

steps = [
    step(
        "create table notas_empenhos ("
            'id SERIAL PRIMARY KEY,'
            'codigo_municipio varchar(10),'
            'exercicio_orcamento varchar(10),'
            'codigo_orgao varchar(10),'
            'codigo_unidade varchar(10),'
            'data_emissao_empenho timestamp,'
            'numero_empenho varchar(20),'
            'data_referencia_empenho varchar(20),'
            'codigo_funcao varchar(20),'
            'codigo_subfuncao varchar(20),'
            'codigo_programa varchar(20),'
            'codigo_projeto_atividade varchar(20),'
            'numero_projeto_atividade varchar(20),'
            'numero_subprojeto_atividade varchar(20),'
            'codigo_elemento_despesa varchar(20),'
            'modalidade_empenho varchar(20),'
            'descricao_empenho text,'
            'valor_anterior_saldo_dotacao decimal,'
            'valor_empenhado decimal,'
            'valor_atual_saldo_dotacao decimal,'
            'tipo_processo_licitatorio varchar(20),'
            'numero_documento_negociante varchar(20),'
            'estado_empenho varchar(20),'
            'numero_nota_anulacao varchar(120),'
            'data_emissao_empenho_substituto timestamp,'
            'numero_empenho_substituto varchar(10),'
            'cd_cpf_gestor varchar(100),'
            'cpf_gestor_contrato varchar(100),'
            'data_contrato timestamp,'
            'numero_contrato varchar(100),'
            'data_realizacao_licitacao timestamp,'
            'numero_licitacao varchar(100),'
            'codigo_tipo_negociante varchar(100),'
            'nome_negociante varchar(255),'
            'endereco_negociante varchar(255),'
            'fone_negociante varchar(100),'
            'cep_negociante varchar(100),'
            'nome_municipio_negociante varchar(100),'
            'codigo_uf varchar(100),'
            'tipo_fonte varchar(100),'
            'codigo_fonte varchar(100)'
        ")",
        "DROP TABLE notas_empenhos"
    )
]