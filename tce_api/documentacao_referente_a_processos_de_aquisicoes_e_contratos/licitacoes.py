from tce_api.base import Base
from itertools import repeat
from datetime import datetime
from model.licitacao import Licitacao
from model.municipio import Municipio
from model.tce_request_monitor import TceRequestMonitor
import pdb
class Licitacoes(Base):
    def __init__(self):
        super().__init__()
        self.initialize_variables_by_method('licitacoes')

    def execute(self):
        try:
            for municipio in Municipio.by_id_range(self.municipio_id):
                self.municipio_id = municipio.id
                licitacoes = []
                for year in range(self.year, datetime.now().year):
                    self.year = year
                    response = self.request_tce_api(self.url_with_params(municipio.codigo, year))
                    for params in response.json()['rsp']['_content']:
                        licitacoes.append(Licitacao(params))
                        Licitacao.save_multiple(licitacoes)
            self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)

    def url_with_params(self, code, year):
        return (
                  '?codigo_municipio=' + code +
                  '&exercicio_orcamento=' + str(year) +
                  '&data_realizacao_autuacao_licitacao=' + str(year) + '0101_' + str(year) + '1231'
                )


