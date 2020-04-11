from models.municipio import Municipio
from models.orgao import Orgao
from models.funcao import Funcao
from models.tipo_unidade_administrativa import TipoUnidadeAdministrativa
from models.ordenador import Ordenador
from models.unidade_gestora import UnidadeGestora
from models.gestor_unidade_gestora import GestorUnidadeGestora
from models.conta_extra_orcamentaria import ContaExtraOrcamentaria
from models.unidade_orcamentaria import UnidadeOrcamentaria
from models.programa import Programa
from models.dado_orcamento import DadoOrcamento
from models.despesa_categoria_economica import DespesaCategoriaEconomica
from models.despesa_elemento_projeto import DespesaElementoProjeto
from models.despesa_projeto_atividade import DespesaProjetoAtividade
from models.orcamento_receita import OrcamentoReceita

from tce_api.documentacao_de_informacoes_basicas.unidades_federativas import UnidadesFederativas
from tce_api.documentacao_de_informacoes_basicas.contas_bancarias import ContasBancarias
# from tce_api.documentacao_referente_a_processos_de_aquisicoes_e_contratos.licitacoes import Licitacoes

from tce_api.basic_requester import BasicRequester
from tce_api.by_city_requester import ByCityRequester

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
ByCityRequester(DadoOrcamento).execute()
ByCityRequester(DespesaCategoriaEconomica).execute()
ByCityRequester(Programa).execute()
ByCityRequester(DespesaElementoProjeto).execute()
ByCityRequester(DespesaProjetoAtividade).execute()
ByCityRequester(OrcamentoReceita).execute()
ByCityRequester(UnidadeOrcamentaria).execute()
# Licitacoes().execute()