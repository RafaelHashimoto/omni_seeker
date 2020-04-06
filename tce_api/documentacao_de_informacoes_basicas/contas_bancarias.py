
from tce_api.base import Base
from models.conta_bancaria import ContaBancaria
from models.municipio import Municipio
from models.orgao import Orgao
from datetime import datetime
import pdb

class ContasBancarias(Base):
    def __init__(self):
        super().__init__()
        self.initialize_variables_by_method('contas_bancarias')

    def execute(self):
        try:
            for municipio in Municipio.by_id_range(self.municipio_id):
                self.municipio_id = municipio.id
                contas_bancarias = []
                for year in range(self.year, datetime.now().year):
                    self.year = year
                    if municipio.codigo in ['057', '099']:
                        orgaos = Orgao.all_by_city_and_year(municipio.codigo, year)
                        for orgao in orgaos:
                            response = self.sanitize_response(
                                self.request_tce_api(self.url_with_params(municipio.codigo, orgao.codigo_orgao)).text
                            )
                            for params in response['rsp']['_content']:
                                contas_bancarias.append(ContaBancaria(params))
                    else:
                        response = self.request_tce_api(self.url_with_params(municipio.codigo))
                        response = self.sanitize_response(response.text)
                        for params in response['rsp']['_content']:
                            contas_bancarias.append(ContaBancaria(params))
                ContaBancaria.save_multiple(contas_bancarias)
            self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)

    def url_with_params(self, codigo, codigo_orgao = ''):
        params = '?codigo_municipio=' + codigo + '&exercicio_orcamento=' + str(self.year) + '00'
        if codigo_orgao != '':
            params = params + '&codigo_orgao=' + codigo_orgao
        return params
