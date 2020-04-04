from tce_api.base import Base
from itertools import repeat
from datetime import datetime
from model.orgao import Orgao
from model.municipio import Municipio

class Orgaos(Base):
    def __init__(self):
        super().__init__()
        self.base_method = 'orgaos.json'
        self.exercicio = 2015

    def execute(self):
        for municipio in Municipio.all():
            orgaos = []
            for exercicio in range(self.exercicio, datetime.now().year):
                self.exercicio = exercicio
                response = self.request_tce_api(self.base_method,
                                            self.url_params(municipio.codigo, exercicio))
                for params in response.json()['rsp']['_content']:
                    orgaos.append(Orgao(params))
                    Orgao.save_multiple(orgaos)

    def url_params(self, codigo, exercicio):
        return ('?codigo_municipio=' + codigo + '&exercicio_orcamento=' + str(exercicio))
