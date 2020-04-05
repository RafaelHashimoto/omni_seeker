
from tce_api.documentacao_de_informacoes_basicas.unidades_federativas import UnidadesFederativas
from tce_api.documentacao_de_informacoes_basicas.municipios import Municipios
from tce_api.documentacao_de_informacoes_basicas.orgaos import Orgaos
from tce_api.documentacao_referente_a_processos_de_aquisicoes_e_contratos.licitacoes import Licitacoes

UnidadesFederativas().execute()
Municipios().execute()
Orgaos().execute()
Licitacoes().execute()
