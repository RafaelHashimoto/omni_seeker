from tce_api.basic_requester import BasicRequester
from tce_api.by_city_requester import ByCityRequester

#Documentacao de Informacoes Basicas - SIM
from models.municipio import Municipio
from models.orgao import Orgao
from models.funcao import Funcao
from models.tipo_unidade_administrativa import TipoUnidadeAdministrativa
from models.ordenador import Ordenador
from models.unidade_gestora import UnidadeGestora
from models.gestor_unidade_gestora import GestorUnidadeGestora
from models.conta_extra_orcamentaria import ContaExtraOrcamentaria
from models.unidade_orcamentaria import UnidadeOrcamentaria
from tce_api.documentacao_de_informacoes_basicas.unidades_federativas import UnidadesFederativas
from tce_api.documentacao_de_informacoes_basicas.contas_bancarias import ContasBancarias

#Documentacao referente ao Orcamento Municipal - SIM
from models.programa import Programa
from models.dado_orcamento import DadoOrcamento
from models.despesa_categoria_economica import DespesaCategoriaEconomica
from models.despesa_elemento_projeto import DespesaElementoProjeto
from models.despesa_projeto_atividade import DespesaProjetoAtividade
from models.orcamento_receita import OrcamentoReceita

#Documentacao referente aos Balancetes - SIM

#Documentacao Comprobatoria de Receitas - SIM

#Documentacao referente a Processos de Aquisicoes e Contratos - SIM
from tce_api.documentacao_referente_a_processos_de_aquisicoes_e_contratos.licitacoes import Licitacoes

#Documentacao Comprobatoria de Despesas - SIM
from models.estorno_liquidacao import EstornoLiquidacao
from models.estorno_pagamento import EstornoPagamento
from models.liquidacao import Liquidacao
from models.anulacao_empenho import AnulacaoEmpenho


#Documentacao de Informacoes Basicas - SIM
UnidadesFederativas().execute()
BasicRequester(Municipio).execute()
BasicRequester(TipoUnidadeAdministrativa).execute()
BasicRequester(Funcao).execute()
ContasBancarias().execute()
ByCityRequester(Orgao).execute()
ByCityRequester(UnidadeGestora).execute()
ByCityRequester(GestorUnidadeGestora).execute()
ByCityRequester(Ordenador).execute()
ByCityRequester(ContaExtraOrcamentaria).execute()
ByCityRequester(UnidadeOrcamentaria).execute()

#Documentacao referente ao Orcamento Municipal - SIM
ByCityRequester(DadoOrcamento).execute()
ByCityRequester(Programa).execute()
ByCityRequester(DespesaCategoriaEconomica).execute()
ByCityRequester(DespesaElementoProjeto).execute()
ByCityRequester(OrcamentoReceita).execute()
ByCityRequester(DespesaProjetoAtividade).execute()

#Documentacao referente aos Balancetes - SIM
# balancete_receita_orcamentaria
# balancete_despesa_orcamentaria
# balancete_despesa_extra_orcamentaria
# balancete_receita_extra_orcamentaria

#Documentacao Comprobatoria de Receitas - SIM
# taloes_extras
# anulacoes_taloes_receitas
# anulacoes_taloes_extras
# taloes_receitas

#Documentacao referente a Processos de Aquisicoes e Contratos - SIM
# publicacoes_editais_licitacoes
# dotacoes_licitacoes
# contratados
# contratos
# itens_licitacoes
# Licitacoes().execute()
# comissoes_licitacoes
# licitantes

#Documentacao Comprobatoria de Despesas - SIM
ByCityRequester(EstornoLiquidacao).execute()
ByCityRequester(EstornoPagamento).execute()
ByCityRequester(AnulacaoEmpenho).execute()
#ByCityRequester(Liquidacao).execute()
# notas_fiscais_liquid
# itens_notas_fiscais
# liquidacoes
# notas_pagamentos
# notas_fiscais
# anulacoes_empenhos
# recursos_empenhos
# notas_empenhos
# despesas_extra_orcamentaria
# cheques_notas_pagamentos

# Documentacao referente a Abertura de Creditos Adicionais - SIM
# destino_realocacoes_orcamentarias
# creditos_adicionais
# fontes_anulacao
# realocacoes_orcamentarias

# Documentacao de Controle do Patrimonio Municipal - SIM
# bens_municipios
# unidade_orcamentaria_bens
# reaval_baixas_bens
# empenhos_bens