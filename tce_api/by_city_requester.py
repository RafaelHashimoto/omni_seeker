from tce_api.base import Base
from datetime import datetime
from models.municipio import Municipio
import pdb
class ByCityRequester(Base):
    def __init__(self, cls):
        super().__init__()
        self.cls = cls
        self.initialize_variables_by_method(self.cls.__table__.name)
        self.array = []

    def execute(self):
        try:
            for municipio in Municipio.by_id_range(self.municipio_id):
                self.municipio_id = municipio.id
                self.array = []
                for year in range(self.year, datetime.now().year):
                    self.year = year
                    self.conditional_requester(municipio.codigo)
                self.cls.save_multiple(self.array)
            self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)

    def conditional_requester(self, codigo):
        if self.cls.__table__.name in self.table_name_list():
            for month in range(1, 12):
                self.insert_response_into_array(
                    self.request_tce_api(
                        self.url_with_params_by_data_referencia(codigo, month)
                    )
                )
        else:
            self.insert_response_into_array(
                self.request_tce_api(self.url_with_params(codigo))
            )

    def insert_response_into_array(self, response):
        for params in response['rsp']['_content']:
            self.array.append(self.cls(params))

    def url_with_params(self, codigo):
        return ('?codigo_municipio=' + codigo + '&exercicio_orcamento=' + str(self.year))

    def url_with_params_by_data_referencia(self, codigo, month):
        return (
            '?codigo_municipio=' + codigo + '&exercicio_orcamento=' + str(self.year) + '&data_referencia=' + str(self.year) + str(month).zfill(2)
        )

    def table_name_list(self):
        return [
            'balancete_despesa_extra_orcamentaria',
            'balancete_receita_extra_orcamentaria',
            'balancete_despesa_orcamentaria',
            'balancete_receita_orcamentaria'
        ]