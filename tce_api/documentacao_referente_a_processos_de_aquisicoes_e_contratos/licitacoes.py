from tce_api.base import Base
from datetime import datetime
from calendar import monthrange
from models.licitacao import Licitacao
from models.municipio import Municipio
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
                    if municipio.codigo in ['057', '099']:
                        for month_range in self.months_range():
                            response = self.request_tce_api(self.url_with_params(municipio.codigo, month_range))
                            for params in response['rsp']['_content']:
                                licitacoes.append(Licitacao(params))
                    else:
                        response = self.request_tce_api(self.url_with_params(municipio.codigo, self.year_range()))
                        for params in response['rsp']['_content']:
                            licitacoes.append(Licitacao(params))
                Licitacao.save_multiple(licitacoes)
            self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)

    def months_range(self):
        dates = []
        for month in range(1, 12):
            dates.append(str(self.year) + str(month).zfill(2)+ '01_' + str(self.year) + str(month).zfill(2) + str(monthrange(self.year, month)[1]).zfill(2))
        return dates

    def year_range(self):
        return str(self.year) + '0101_' + str(self.year) + '1231'

    def url_with_params(self, code, date):
        return (
                  '?codigo_municipio=' + code +
                  '&exercicio_orcamento=' + str(self.year) +
                  '&data_realizacao_autuacao_licitacao=' + date
                )
