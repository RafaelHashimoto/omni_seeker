from tce_api.base import Base
from itertools import repeat
from datetime import datetime
from model.licitacao import Licitacao
from model.municipio import Municipio
import pdb
class Licitacoes(Base):
    def __init__(self):
        super().__init__()
        self.base_method = 'licitacoes.json'
        self.exercicio = 2015

    def execute(self):
        for municipio in Municipio.all():
            licitacoes = []
            for exercicio in range(self.exercicio, datetime.now().year):
                self.exercicio = exercicio
                response = self.request_tce_api(self.base_method,self.url_with_params(municipio.codigo, exercicio))
                for params in response.json()['rsp']['_content']:
                    licitacoes.append(Licitacao(params))
                    Licitacao.save_multiple(licitacoes)

    def url_with_params(self, city, year):
        return (
                  '?codigo_municipio=' + city +
                  '&exercicio_orcamento=' + str(year) +
                  '&data_realizacao_autuacao_licitacao=' + str(year) + '0101_' + str(year) + '1231'
                )


